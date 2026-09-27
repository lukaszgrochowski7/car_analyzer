def main():
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


def input_1(): 

    print("Dodawanie samochodu, jeżeli nie chcesz podać wartości, zostaw pole puste i naciśnij enter")
    brand = input("Podaj markę: ").strip() or None
    model = input("Podaj model: ").strip() or None
    transmission = input("Podaj skrzynię biegów: ").strip() or None
    year = int(input("Podaj rok produkcji: "))
    fuel_type = input("Podaj rodzaj paliwa: ").strip() or None
    mileage = int(input("Podaj przebieg: "))
    price_usd = float(input("Podaj cenę w USD: "))

    add_car(brand, model, transmission, year, fuel_type, mileage, price_usd)