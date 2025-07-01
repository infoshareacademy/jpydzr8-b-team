from waliduj_login_haslo import waliduj_login_haslo
from reset_hasla import reset_hasla

def logowanie(nazwa_pliku) -> str | bool:
    
    print("[logowanie] Wpisz 'q' aby wrócić do menu głównego lub 'reset' aby zresetować hasło.")

    while True:
        login = input("[logowanie] Prosze podać login: ")
        if login == 'q':
            break
        if login == 'reset':
            reset_hasla("baza_uzytkownikow.txt")
            continue
        haslo = input("[logowanie] Proszę podać hasło: ")
        if haslo == 'q':
            break
        if haslo == 'reset':
            if reset_hasla("baza_uzytkownikow.txt"):
                continue
        id_uzytkownika = waliduj_login_haslo(login, haslo, nazwa_pliku="baza_uzytkownikow.txt")
        if id_uzytkownika:
            print(f"[logowanie] Zalogowano użytkownika: {login}.")
            return id_uzytkownika
        print("[logowanie] Błędny login lub haslo - spróbuj ponownie.")
        return False
