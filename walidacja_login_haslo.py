def waliduj_login_haslo(login, haslo, nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            for linia in plik:
                dane = linia.strip().split(';')
                if len(dane) >= 7:
                    if dane[5] == login and dane[6] == haslo:
                        return True
        return False
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
        return False
    
waliduj_login_haslo