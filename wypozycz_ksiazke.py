import pandas as pd
import datetime as datetime

plik = 'baza_ksiazek.txt'

def wczytanie_bazy_ksiazek():
    df = pd.read_csv('baza_ksiazek.txt',sep = ';', names = ['ID Książki', 'Autor', 'Tytuł', 'Ilość'],
                     index_col = False)
    df.to_string()
    return df

# def zalogowany():
#     zalogowany = True

def wypozycz_ksiazke():
    # zalogowany()
    print('Jesteś zalogowany')
    df = wczytanie_bazy_ksiazek()
    print(df)
    while True:
        id_wypozyczonej_ksiazki = input('Wypożycz książkę podając ID książki (x spowoduje zakończenie): ').lower()
        if id_wypozyczonej_ksiazki == 'x':
            break
        wypozyczona_ksiazka = df[df["ID Książki"] == int(id_wypozyczonej_ksiazki)]
        index_wypozyczonej_ksiazki = wypozyczona_ksiazka.index
        i = index_wypozyczonej_ksiazki[0]
        if df.at[i, 'Ilość'] == 0:
            print('Książka nie jest dostęþna')
        else:
            df.at[i, 'Ilość'] -= 1
            data_wypozyczenia = datetime.date.today()
            data_oddania = data_wypozyczenia + datetime.timedelta(days=30)
            df.to_csv('baza_ksiazek.txt', index = False, header = False, sep = ';')
            print(f'Wypożyczono książkę: {df.at[i, 'Tytuł']}, {df.at[i, 'Autor']}, '
                  f'dnia {data_wypozyczenia.isoformat()}, data oddania {data_oddania.isoformat()}')
        print(df)

print(wypozycz_ksiazke())
