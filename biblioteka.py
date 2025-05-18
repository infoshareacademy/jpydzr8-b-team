import pandas as pd

def wczytanie_bazy_ksiazek(baza_ksiazek):
    df = pd.read_csv('baza_ksiazek.txt', sep=';', names=['ID Książki', 'Autor', 'Tytuł', 'Ilość'])
    df.astype(str)
    return df

plik = 'baza_ksiazek.txt'
#print(wczytanie_bazy_książek(plik))