class Uzytkownik:
    def __init__(self, numer, imie, nazwisko, wiek, email, login, haslo, zainteresowania):
        self.numer = numer
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.email = email
        self.login = login
        self.haslo = haslo
        self.zainteresowania = zainteresowania

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'a', encoding='utf-8') as plik:
            plik.write(f"{self.numer:03d};{self.imie};{self.nazwisko};{self.wiek};{self.email};"
                       f"{self.login};{self.haslo};{self.zainteresowania}\n")

def numer_karty(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            linie = plik.readlines()
            if not linie:
                return 1
            ostatnia_linia = linie[-1].strip()
            numer = int(ostatnia_linia.split(';')[0])
            return numer + 1
    except (FileNotFoundError, IndexError, ValueError):
        return 1