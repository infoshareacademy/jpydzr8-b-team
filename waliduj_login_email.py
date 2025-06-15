def waliduj_login_email(login, email, nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            for linia in plik:
                dane = linia.strip().split(';')
                if len(dane) >= 7:
                    if dane[5] == login and dane[4] == email:
                        return True
        return False
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony.")
        return False