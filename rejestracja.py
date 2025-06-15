
from klasa_uzytkownik import Uzytkownik, numer_karty
from waliduj_email import waliduj_email
def rejestracja(nazwa_pliku):
    istniejace_loginy = set()
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            for linia in plik:
                dane = linia.strip().split(';')
                if dane:
                    istniejace_loginy.add(dane[5])
    except FileNotFoundError:
        pass

    while True:
        login = input("Proszę podać login: ").strip()
        if login in istniejace_loginy:
            print("Ten login już istnieje. Wybierz inny.")
        else:
            break

    while True:
        haslo = input("Proszę podać hasło: ")
        if haslo == input("Proszę powtórzyć hasło: "):
            break
        print("Podane hasła się różnią. Spróbuj jeszcze raz.")

    while True:
        imie = input("Proszę podać imię: ").strip()
        if imie.isalpha():
            break
        print("Niepoprawny format - spróbuj ponownie.")

    while True:
        nazwisko = input("Proszę podać nazwisko: ").strip()
        if nazwisko.isalpha():
            break
        print("Niepoprawny format - spróbuj ponownie.")

    while True:
        wiek = input("Proszę podać wiek: ").strip()
        if wiek.isdigit() and 10 <= int(wiek) <= 100:
            break
        print("Niepoprawny format - spróbuj ponownie.")

    while True:
        email = input("Proszę podać email: ").strip()
        if '@' not in email or "." not in email:
            print("Niepoprawny format - spróbuj ponownie.")
            continue
        if waliduj_email(email, "baza_uzytkownikow.txt"):
            print("Ten adres e-mail już istnieje w bazie.")
            continue
        break


    zainteresowania = input("Proszę podać zainteresowania: ")
    numer =  numer_karty(nazwa_pliku)


    u = Uzytkownik(
        numer=numer,
        imie=imie,
        nazwisko=nazwisko,
        wiek=wiek,
        email=email,
        login=login,
        haslo=haslo,
        zainteresowania=zainteresowania
    )

    u.zapisz_do_pliku(nazwa_pliku)
    print(f"Użytkownik {login} został zarejestrowany z numerem karty {numer:03d}.")

# rejestracja("/Users/jacek.c/desktop/python_project/oop/uzytkownicy2.txt")