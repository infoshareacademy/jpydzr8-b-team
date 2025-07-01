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
    print("Proszę uzupelnić dane do rejestracji. Wpisz 'q', aby wrócić do menu głównego.")
    while True:
        login = input("[rejestracja] Proszę podać login: ").strip()
        if login == 'q':
            return
        if login in istniejace_loginy:
            print("[rejestracja] Ten login już istnieje. Wybierz inny.")
        else:
            break

    while True:
        haslo = input("[rejestracja] Proszę podać hasło: ")
        if haslo == "q":
            return
        if haslo == input("[rejestracja] Proszę powtórzyć hasło: "):
            break
        print("[rejestracja] Podane hasła się różnią. Spróbuj jeszcze raz.")

    while True:
        imie = input("[rejestracja] Proszę podać imię: ").strip()
        if imie == 'q':
            return
        if imie.isalpha():
            break
        print("[rejestracja] Niepoprawny format - spróbuj ponownie.")

    while True:
        nazwisko = input("[rejestracja] Proszę podać nazwisko: ").strip()
        if nazwisko == 'q':
            return
        if nazwisko.isalpha():
            break
        print("[rejestracja] Niepoprawny format - spróbuj ponownie.")

    while True:
        wiek = input("[rejestracja] Proszę podać wiek: ").strip()
        if wiek == 'q':
            return
        if wiek.isdigit() and 10 <= int(wiek) <= 100:
            break
        print("[rejestracja] Niepoprawny format - spróbuj ponownie.")

    while True:
        email = input("Proszę podać email: ").strip()
        if email == 'q':
            return
        if '@' not in email or "." not in email:
            print("[rejestracja] Niepoprawny format - spróbuj ponownie.")
            continue
        if waliduj_email(email, "baza_uzytkownikow.txt"):
            print("[rejestracja] Ten adres e-mail już istnieje w bazie.")
            continue
        break
  
    zainteresowania = input("[rejestracja] Proszę podać zainteresowania: ")
    if zainteresowania == 'q':
        return
            
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
