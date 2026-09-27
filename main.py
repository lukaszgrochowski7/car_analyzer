from database import add_car, find_car


def main():
    while True:
            
        print("Witaj!")
        print("Wybierz opcję:")
        print("1. Dodaj samochód")
        print("2. wyszukaj samochód")
        print("3. wyjdź")
        while True:
            try:
                input_option = input("Wybierz opcję (1, 2 lub 3): ")
                if input_option != "1" and input_option != "2" and input_option != "3":
                    raise ValueError
            except ValueError :
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
            else:
                break
        if input_option == "1":
            input_1()
        if input_option == "2":
            input_2()
        

def input_1(): 

    print("Dodawanie samochodu, jeżeli nie chcesz podać wartości, zostaw pole puste i naciśnij enter")
    brand = input("Podaj markę: ").strip() or None
    model = input("Podaj model: ").strip() or None
    transmission = input("Podaj skrzynię biegów: ").strip() or None
    while True:
        try:
            year = int(input("Podaj rok produkcji: "))
            if year > 2025 or year < 1900:
                raise ValueError
        except ValueError:
            print("Nieprawidłowy rok produkcji. Spróbuj ponownie.")
        else:
            break
    fuel_type = input("Podaj rodzaj paliwa: ").strip() or None
    while True:
        try:
            mileage = int(input("Podaj przebieg: "))
            if mileage < 0:
                raise ValueError
        except ValueError:
            print("Nieprawidłowy przebieg. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            price_usd = float(input("Podaj cenę w USD: "))
            if price_usd < 0:
                raise ValueError
        except ValueError:
            print("Nieprawidłowa cena. Spróbuj ponownie.")
            
        else:
            break
    add_car(brand, model, transmission, year, fuel_type, mileage, price_usd)
    print("Pomyślnie dodano samochód")

def input_2():
    print("Wyszukiwanie samochodu, jeżeli nie chcesz podać wartości, zostaw pole puste i naciśnij enter")
    brand = input("Podaj markę: ").strip() or None
    model = input("Podaj model: ").strip() or None
    while True:
        options = ["Manual","Automatic"]
        try:
            transmission = input("Podaj skrzynię biegów: [Manual/Automatic] ").strip() or None
            if transmission == "" or transmission not in options:
                raise ValueError
        except ValueError:
            print("Nieprawidłowa skrzynia biegów. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            min_year = input("Podaj minimalny rok produkcji: ").strip()
            if min_year == "":
                min_year = None
            else:
                min_year = int(min_year)
                if min_year > 2025 or min_year < 1900:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowy rok produkcji. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            max_year = input("Podaj maksymalny rok produkcji: ").strip()
            if max_year == "":
                max_year = None
            else:
                max_year = int(max_year)
                if max_year > 2025 or max_year < 1900:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowy rok produkcji. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            min_mileage = input("Podaj minimalny przebieg: ").strip()
            if min_mileage == "":
                min_mileage = None
            else:
                min_mileage = int(min_mileage)
                if min_mileage < 0:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowy przebieg. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            max_mileage = input("Podaj maksymalny przebieg: ").strip()
            if max_mileage == "":
                max_mileage = None
            else:
                max_mileage = int(max_mileage)
                if max_mileage < 0 or max_mileage < min_mileage:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowy przebieg. Spróbuj ponownie.")
        else:
            break

    while True:
        try:
            min_price = input("Podaj minimalną cenę w USD: ").strip()
            if min_price == "":
                min_price = None
            else:
                min_price = float(min_price)
                if min_price < 0:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowa cena. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            max_price = input("Podaj maksymalną cenę w USD: ").strip()
            if max_price == "":
                max_price = None
            else:
                max_price = float(max_price)
                if max_price < 0 or max_price < min_price:
                    raise ValueError
        except ValueError:
            print("Nieprawidłowa cena. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            by = input("Podaj kolumnę do sortowania: [brand, model, transmission, year, fuel_type, mileage, price_usd] ").strip() or None
            if by is not None and by not in ["brand", "model", "transmission", "year", "fuel_type", "mileage", "price_usd"]:
                raise ValueError
        except ValueError:
            print("Nieprawidłowa kolumna. Spróbuj ponownie.")
        else:
            break
    while True:
        try:
            order = input("Podaj kolejność sortowania: [ASC, DESC] ").strip() or None
            if order is not None and order not in ["ASC", "DESC"]:
                raise ValueError
        except ValueError:
            print("Nieprawidłowa kolejność. Spróbuj ponownie.")
        else:
            break
    print(find_car(brand=brand, model=model, transmission=transmission, min_year=min_year, max_year=max_year, min_mileage=min_mileage, max_mileage=max_mileage, min_price=min_price, max_price=max_price, by=by, order=order))

main()