from waliduj_login_haslo import waliduj_login_haslo

def logowanie(nazwa_pliku):
    
    print("Wpisz 'q' aby wrócić do menu głównego.")

    while True:
        zalogowany = False
        login = input("Prosze podać login: ")
        if login == 'q':
            break
        haslo = input("Proszę podać hasło: ")
        if haslo == 'q':
            break
        if waliduj_login_haslo(login, haslo, nazwa_pliku="baza_uzytkownikow.txt"):
            print(f"Zalogowano uytkownika po login:{login} i haslo:{haslo}")
            zalogowany = True
            if zalogowany:
                break
        else:
            print("Błędny login lub haslo - spróbuj ponownie.")
    return zalogowany      
        
