
class Wypowiedzenie:
    def __init__(self, id: str):
        self.__id = str(id).strip()
        self.__registered: str = 'baza_uzytkownikow.txt'
        self.__deregistered: str = 'baza_wyrejestrowani.txt'
        self.__indeks_kasowany: int = 0
        self.__rekord_kasowany: list =[]
        self.__baza: list =[]

    def deaktywuj(self) -> bool:
        if self.__id:
            self.__otworz_baze()
            self.__indeks_kasowany = self.__zwroc_indeks_rekordu()
            if self.__indeks_kasowany is not None:
                self.__przenies_i_kasuj()
                self.__zapisz()
                return True
        return False

    def __otworz_baze(self):
        '''Pobiera dane do zmiennej obiektowej .__baza'''
        with open(self.__registered, 'r') as f:
            lines = f.readlines()
            self.__baza = [(line.strip('\n').split(';')) for line in lines]

    def __przenies_i_kasuj(self):
        self.__rekord_kasowany = self.__baza[self.__indeks_kasowany]
        self.__rekord_kasowany[8] = False
        self.__dopisz_do_wyrejestrowanych()
        self.__baza.pop(self.__indeks_kasowany)

    def __zapisz(self):
        '''Rozróżnia czy baza ma jeden rekord czy więcej, i zapisuje
        na nowo bazę zarejestrowanych, usuwając poprzednie dane.
        '''
        with open(self.__registered,'w') as f:
            if isinstance(self.__baza[0], list):
                for i, rekord in enumerate(self.__baza):
                    f.write(';'.join([str(element) for element in rekord]) + '\n')
            else:
                f.write(';'.join([str(element) for element in self.__baza]) + '\n')

    def __zwroc_indeks_rekordu(self) -> int | None:
        ''' Tworzy listę samych ID wyjętych z rekordów z bazy.
        Lista IDs będzie miała dokładnie tę samą długość co baza.
        List.index() zwraca index listy pod którym wystepuje ID.
        :return: numeric / None kiedy ID nie występuje.
        '''
        lista = [line[0] for line in self.__baza]
        try:
            return lista.index(self.__id)
        except ValueError:
            return None

    def __dopisz_do_wyrejestrowanych(self):
        '''Dopisuje rekord na końcu pliku. Jesli plik nie istnieje to
        zostanie utworzony w ramach projektu wg zmiennej '.__deregistered',
        a rekord zostanie zapisany.'''
        with open(self.__deregistered, 'a') as f:
            if self.__rekord_kasowany:
                f.write(';'.join([str(element) for element in self.__rekord_kasowany]) + '\n')

# umowa = Wypowiedzenie()
# print(umowa)