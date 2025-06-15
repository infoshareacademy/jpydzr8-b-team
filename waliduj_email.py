def waliduj_email(email, nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) > 4 and dane[4].strip().lower() == email.strip().lower():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{nazwa_pliku}' nie został znaleziony.")
        return False
