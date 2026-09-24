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
        "make_year" INT,
        "fuel_type" TEXT,
        "engine_capacity" INT,
        "mileage" INT,
        "price" INT
        
        
        );

    """)
    conn.commit()
    conn.close()
def add_data(brand,model,transmission,make_year,fuel_type,engine_capacity,mileage,price):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO "cars" (brand,model,transmission,make_year,fuel_type,engine_capacity,mileage,price)
        VALUES(?,?,?,?,?,?,?,?)
        """,(brand,model,transmission,make_year,fuel_type,engine_capacity,mileage,price))
    conn.commit()
    conn.close()
def data():
    with open("pre-ownedcars.csv","r",newline="",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for wiersz in reader:
            add_data(
                wiersz["brand"],
                wiersz["model"],
                wiersz["transmission"],
                wiersz["make_year"],
                wiersz["fuel_type"],
                wiersz["engine_capacity"],
                wiersz["mileage"],
                wiersz["price"]
            )

if __name__ == "__main__":
    create_table()
    data()