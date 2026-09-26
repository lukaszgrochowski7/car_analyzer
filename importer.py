import csv
import sqlite3

def create_table():
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            "id" INTEGER PRIMARY KEY,
            "brand" TEXT NOT NULL,
            "model" TEXT NOT NULL,
            "transmission" TEXT NOT NULL,
            "year" INT,
            "fuel_type" TEXT,
            "mileage" INT,
            "price_usd" INT
        );
    """)
    conn.commit()
    conn.close()

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def data():
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    with open("used_cars_10M_2025.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        batch = []

        for wiersz in reader:
            batch.append((
                wiersz["brand"],
                wiersz["model"],
                wiersz["transmission"],
                to_int(wiersz["year"]),
                wiersz["fuel_type"],
                to_int(wiersz["mileage_km"]),
                to_int(wiersz["price_usd"])
            ))

            if len(batch) >= 10000:
                c.executemany("""
                    INSERT INTO cars (brand,model,transmission,year,fuel_type,mileage,price_usd)
                    VALUES(?,?,?,?,?,?,?)
                """, batch)
                conn.commit()
                batch.clear()

        if batch:
            c.executemany("""
                INSERT INTO cars (brand,model,transmission,year,fuel_type,mileage,price_usd)
                VALUES(?,?,?,?,?,?,?)
            """, batch)
            conn.commit()

    conn.close()

if __name__ == "__main__":
    create_table()
    data()