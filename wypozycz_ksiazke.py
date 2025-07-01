import pandas as pd
import datetime as datetime


plik = 'baza_ksiazek.txt'

def wczytanie_bazy_ksiazek():
    df = pd.read_csv('baza_ksiazek.txt', sep=';', names=['ID Książki', 'Autor', 'Tytuł', 'Ilość'],
                     index_col=False)
    df['Ilość'] = df['Ilość'].astype(int)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    return df

def wypozycz_ksiazke():
    # if logowanie():
    #     print('Jesteś zalogowany')
    df_new = wczytanie_bazy_ksiazek()
    print(df_new.to_string(index=False))  # Wyświetlanie bez indeksu

    wypozyczone = []  # lista wypożyczonych książek

    while len(wypozyczone) < 5:
        id_wypozyczonej_ksiazki = input(
            f'Wypożycz książkę podając ID książki (x kończy wybór, wypożyczono {len(wypozyczone)}/5): ').lower()

        if id_wypozyczonej_ksiazki == 'x':
            print("Zakończono wybieranie książek.")
            break

        if not id_wypozyczonej_ksiazki.isdigit():
            print("Niepoprawne ID. Podaj liczbę całkowitą.")
            continue

        id_wypozyczonej_ksiazki = int(id_wypozyczonej_ksiazki)

        if id_wypozyczonej_ksiazki not in df_new["ID Książki"].values:
            print("Nie ma książki o takim ID.")
            continue

        wypozyczona_ksiazka = df_new[df_new["ID Książki"] == id_wypozyczonej_ksiazki]
        index_wypozyczonej_ksiazki = wypozyczona_ksiazka.index[0]

        if df_new.at[index_wypozyczonej_ksiazki, 'Ilość'] == 0:
            print('Książka nie jest dostępna.')
            continue
        else:
            df_new.at[index_wypozyczonej_ksiazki, 'Ilość'] -= 1
            data_wypozyczenia = datetime.date.today()
            data_wypozyczenia_str = data_wypozyczenia.isoformat()
            data_oddania = data_wypozyczenia + datetime.timedelta(days=30)
            data_oddania_str = data_oddania.isoformat()
            tytul = df_new.at[index_wypozyczonej_ksiazki, 'Tytuł']
            autor = df_new.at[index_wypozyczonej_ksiazki, 'Autor']
            wypozyczone.append((tytul, autor, data_wypozyczenia_str, data_oddania_str))
            print(f'Wypożyczono książkę: {tytul}, {autor}, '
                  f'data wypożyczenia: {data_wypozyczenia_str}, '
                  f'data oddania: {data_oddania_str}')

    df_new.to_csv('baza_ksiazek.txt', index=False, header=False, sep=';')

    print('\nPodsumowanie wypożyczeń:')
    for ksiazka in wypozyczone:
        print(f'Tytuł: {ksiazka[0]}, Autor: {ksiazka[1]}, Wypożyczono: {ksiazka[2]}, Oddać do: {ksiazka[3]}')

    return wypozyczone
