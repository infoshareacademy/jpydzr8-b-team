import pandas as pd
from rejestracja import *
from logowanie import *
from wypozycz_ksiazke import wypozycz_ksiazke, wczytanie_bazy_ksiazek

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Zaloguj sie")
        print("2. Zaloz konto")
        print("3. Biblioteka")
        print("4. Wyjdz")
        wybor = input("Wybierz opcje (1-4): ")
        if wybor == "1":
            logowanie("oop/baza_uzytkownikow.txt")
            wypozycz_ksiazke()
        elif wybor == "2":
            rejestracja("baza_uzytkownikow.txt")
        elif wybor == "3":
            print(wczytanie_bazy_ksiazek())
        elif wybor == "4":
            print("Do zobaczenia !")
            break
        else:
            print("Nieprawidlowy wybor, sprobuj ponownie.")
menu()

