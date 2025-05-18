import pandas as pd
from rejestracja import *
from biblioteka import *
from logowanie import *


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Zaloguj sie")
        print("2. Zaloz konto")
        print("3. Biblioteka")
        print("4. Wyjdz")
        wybor = input("Wybierz opcje (1-4): ")
        if wybor == "1":
            logowanie("baza_uzytkownikow.txt")
        elif wybor == "2":
            rejestracja("baza_uzytkownikow.txt")
        elif wybor == "3":
            print(wczytanie_bazy_ksiazek("baza_ksiazek.txt"))
        elif wybor == "4":
            print("Do zobaczenia !")
            break
        else:
            print("Nieprawidlowy wybor, sprobuj ponownie.")
menu()

