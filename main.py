from logowanie import logowanie
from rejestracja import *
from wypozycz_ksiazke import wypozycz_ksiazke, wczytanie_bazy_ksiazek
from menu_po_zalogowaniu import menu_po_zalogowaniu

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Zaloguj się")
        print("2. Zaloż konto")
        print("3. Biblioteka")
        print("4. Wyjdź")
        wybor = input("Wybierz opcję (1-4): ")
        if wybor == "1":
            id_uzytkownika = logowanie("baza_uzytkownikow.txt")

            # zwraca True kiedy hasło było zresetowane,
            # więc wymagamy ponownego zalogowania się.
            # False oznacza logowanie bez resetowania.
            if id_uzytkownika == True:
                continue

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
            print("Nieprawidłowy wybór, spróbuj ponownie.")

#
if __name__ == "__main__":
    menu()