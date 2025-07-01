from wypozycz_ksiazke import wypozycz_ksiazke
import os


ID = '001'
imie = 'Adam'
nazwisko = 'Talaga'
lista_wypozyczonych_ksiazek = wypozycz_ksiazke()
karta_uzytkowanika_sciezka = f'{ID}_{imie}_{nazwisko}.txt'


def karta_czytelnika(ID, karta_uzytkowanika_sciezka, lista_wypozyczonych_ksiazek):

    mode = 'a' if os.path.exists(karta_uzytkowanika_sciezka) else 'w'
    with open(karta_uzytkowanika_sciezka, mode) as f:
        f.write(lista_wypozyczonych_ksiazek)

karta_czytelnika(ID, karta_uzytkowanika_sciezka, lista_wypozyczonych_ksiazek)