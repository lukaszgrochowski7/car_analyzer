import sqlite3
def add_car(brand,model,transmission,make_year,fuel_type,engine_capacity,mileage,price):
    try:
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute("""
        INSERT INTO "cars" (brand,model,transmission,make_year,
        fuel_type,engine_capacity,mileage,price)
        VALUES(?,?,?,?,?,?,?,?)
        """,(brand,model,transmission,make_year,fuel_type,engine_capacity,mileage,price))
        conn.commit()
        conn.close()
    except Exception:
        print("Dodanie samochodu nieudane!, sprawdź czy podałeś wszystkie wartości własciwe")
    else:
        print("Pomyślnie dodano samochód")
def get_cars():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cars")

    cars = cursor.fetchall()

    conn.close()

    return cars

def search_cars():
    ...


