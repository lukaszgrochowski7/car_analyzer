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
            by=None,
            order=None
            ):
    parameters = []
    conditions = [] 
    parameters_by = ""
    parameters_order = ""
    if brand is not None:
        conditions.append("brand = ?")
        parameters.append(brand)
    if min_price is not None:
        conditions.append("price_usd > ?")
        parameters.append(min_price)
    if max_price is not None:
        conditions.append("price_usd < ?")
        parameters.append(max_price)
    if min_mileage is not None:
        conditions.append("mileage > ?")
        parameters.append(min_mileage)
    if max_mileage is not None:
        conditions.append("mileage < ?")
        parameters.append(max_mileage)
    if min_year is not None:
        conditions.append("year > ?")
        parameters.append(min_year)
    if max_year is not None:
        conditions.append("year < ?")
        parameters.append(max_year)
    if by is not None:
        if by not in ["brand", "model", "transmission", "year", "fuel_type", "mileage", "price_usd"]:
            raise ValueError("Invalid 'by' parameter. Must be one of: brand, model, transmission, year, fuel_type, mileage, price_usd")
        else:
            parameters_by = by
    if order is not None:
        if order not in ["ASC", "DESC"]:
            raise ValueError("Invalid 'order' parameter. Must be either 'ASC' or 'DESC'")
        else:
            parameters_order = order
    conn = sqlite3.connect("cars.db")
    c = conn.cursor()
    query = "SELECT * FROM cars"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    if parameters_by:
        query += f" ORDER BY {parameters_by}"
        if parameters_order:
            query += f" {parameters_order}"
        #todo przypadek gdy mamy by ale nie mamy order
    c.execute(query,tuple(parameters))
    cars = c.fetchall()
    conn.close()
    return cars 
if __name__ == "__main__":
    pass

