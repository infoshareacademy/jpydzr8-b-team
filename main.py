import pandas as pd
from rejestracja import *
from wypozycz_ksiazke import wypozycz_ksiazke, wczytanie_bazy_ksiazek
from menu_po_zalogowaniu import menu_po_zalogowaniu
from logowanie import logowanie

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Zaloguj sie")
        print("2. Zaloz konto")
        print("3. Biblioteka")
        print("4. Wyjdz")
        wybor = input("Wybierz opcje (1-4): ")
        if wybor == "1":
            id_uzytkownika = logowanie("baza_uzytkownikow.txt")
            if id_uzytkownika:
                menu_po_zalogowaniu(id_uzytkownika)
        elif wybor == "2":
            rejestracja("baza_uzytkownikow.txt")
        elif wybor == "3":
            print(wczytanie_bazy_ksiazek())
        elif wybor == "4":
            print("Do zobaczenia !")
            break
        else:
            print("Nieprawidlowy wybor, sprobuj ponownie.")


if "__name__" == "__main__":
    menu()