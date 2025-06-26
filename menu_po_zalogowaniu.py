from wypozycz_ksiazke import wypozycz_ksiazke, wczytanie_bazy_ksiazek
from zmiana_danych import ZmianaDanych

def menu_po_zalogowaniu(id_uzytkownika):
    while True:
        print("1. Wypożycz książkę.")
        print("2. Zmiana danych.")
        print("3. Powrót do Menu Głównego.")
        wybor2 = input("Wybierz opcje (1-3): ")
        if wybor2 == "1":
            wypozycz_ksiazke()
        elif wybor2 == "2":
            ZmianaDanych().edycja_danych_uzytkownika(id_uzytkownika)
        elif wybor2 == "3":
            break
        else:
            print("Nieprawidłowy wybór")