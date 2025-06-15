from waliduj_login_haslo import waliduj_login_haslo
from reset_hasla import reset_hasla

def logowanie(nazwa_pliku):
    
    print("Wpisz 'q' aby wrócić do menu głównego lub 'reset' aby zresetować hasło.")

    while True:
        login = input("Prosze podać login: ")
        if login == 'q':
            break
        if login == 'reset':
            reset_hasla("baza_uzytkownikow.txt")
        haslo = input("Proszę podać hasło: ")
        if haslo == 'q':
            break
        if haslo == 'reset':
            reset_hasla("baza_uzytkownikow.txt")
        id_uzytkownika = waliduj_login_haslo(login, haslo, nazwa_pliku="baza_uzytkownikow.txt")
        if id_uzytkownika:
            print(f"Zalogowano uytkownika po login:{login} i haslo:{haslo}")
            return id_uzytkownika
        print("Błędny login lub haslo - spróbuj ponownie.")
        return False      
        
