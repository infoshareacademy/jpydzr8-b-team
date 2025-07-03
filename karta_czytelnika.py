import os

def karta_czytelnika(u_id, lista_wypozyczonych_ksiazek):
    czytelnia = 'czytelnia/' + u_id + '.txt'
    mode = 'a' if os.path.exists(czytelnia) else 'w'
    with open(czytelnia, mode) as f:
        if isinstance(lista_wypozyczonych_ksiazek[0], tuple):
            for i, rekord in enumerate(lista_wypozyczonych_ksiazek):
                f.write(';'.join([str(element) for element in rekord]) + '\n')
        else:
            f.write(';'.join([str(element) for element in lista_wypozyczonych_ksiazek]) + '\n')