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
    
def find_car(brand=None,
            min_price=None,
            max_price=None,
            min_mileage=None,
            max_mileage=None,
            min_year=None,
            max_year=None,
            ):
    parameters = []
    conditions = [] 
    if brand is not None:
        conditions.append("brand = ?")
        parameters.append(brand)
    if min_price is not None:
        conditions.append("price > ?")
        parameters.append(min_price)
    if max_price is not None:
        conditions.append("price < ?")
        parameters.append(max_price)
    if min_mileage is not None:
        conditions.append("mileage > ?")
        parameters.append(min_mileage)
    if max_mileage is not None:
        conditions.append("mileage < ?")
        parameters.append(max_mileage)
    if min_year is not None:
        conditions.append("make_year > ?")
        parameters.append(min_year)
    if max_year is not None:
        conditions.append("make_year < ?")
        parameters.append(max_year)
    conn = sqlite3.connect("cars.db")
    c = conn.cursor()
    query = "SELECT * FROM cars"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    c.execute(query,tuple(parameters))
    cars = c.fetchall()
    conn.close()
    return cars 
if __name__ == "__main__":
    pass

