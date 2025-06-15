import usuwanie_danych as umowa

class ZmianaDanych:
    '''
    Klasa obsługuje zmianę wszystkich danych personalnych czytelnika, poza ID.
    Posiada jedną instrukcję wejściową 'edycja_danych_uzytkownika' która wymaga
    wyłącznie: ID. Jako wzór służy do wyszukiwania rekordu danych z użyciem metody
    list.index(). Zmiana danych następuje bezpośrednio w zmiennej LST_BAZA,
    poczym cała baza zostaje nadpisana spowrotem do pierwotnego pliku .txt.
    Plik bazy_uzytkownika zaklada stały porządek elementów każdego rekordu, zob.
    atrybuty klasy .__INDEKSY_REKORDU.
    '''
    __STR_BAZA = 'baza_uzytkownikow.txt'
    __INDEKSY_REKORDU = dict(id=0, imie=1, nazwisko=2, wiek=3, email=4, login=5, haslo=6, zainteresowania=7, zarejestrowany=8)
    __LST_BAZA = []
    __ZNAK_REZYGNACJA = 'q'

    def __init__(self):
        self.__id: str = ''
        self.__indeks_rekordu = None
        self.__pozycja_elementu = None
        self.__wartosc_elementu = None
        self.__stara_wartosc_elementu = None


    def edycja_danych_uzytkownika(self, id: str = ''):
        ''' Główna funkcja zbierająca informacje
        do atrybutów obiektu, poczym z nich następuje
        zapis zmian w rekordzie danych, i aktualizacja
        bazy danych w txt.
        :return: None
        '''
        # prewencyjnie 'str'
        id = str(id).strip()

        # brak argumentu więc odmów
        if not id:
            self.komunikat('Nie wprowadzono ID użytkownika.')
            return False
        self.__id = id

        # wgraj bazę do class.__LST_BAZA
        ZmianaDanych.__import_bazy()

        # uzyskaj rekord usera z bazy
        self.__indeks_rekordu = self.__zwroc_nr_rekordu(dla_id=id)

        # brak dopasowania więc odmów
        if self.__indeks_rekordu is None:
            self.komunikat(f'Nie ma użytkownika o numerze {id}.')
            return False

        # user zrezygnował więc wycofaj się
        if not self.__menu_wybierz_dane():
            return False

        # zebranie danych
        if not self.__proceduj_wybor():
            return False

        # próba zmiany w .__LST_BAZA
        if not self.__zmiana():
            self.komunikat('Coś poszło nie tak. Błąd został zarejestrowany. Spróbuj ponownie innym razem.')
            return False

        # rejestracja zmian w bazie docelowej
        self.__aktualizacja_bazy_txt()
        self.komunikat('Zmiany zostały wprowadzone.', monit=False)
    #


    def __menu_wybierz_dane(self) -> bool:
        ''' User decyduje który 'element' danych zmienia,
        albo rezygnuje i wraca do Menu Głównego. Funkcja
        zwraca True, gdy zapisuje pozycję elementu do
        zmiany w atrybucie instancji, inaczej zwraca False.
        '''
        while True:
            # decyzja usera
            element = self.__odpowiedz_z_menu()
            try:
                element = int(element)
            except ValueError:
                # q - rezygnacja i powrót do Menu Głównego
                if element == ZmianaDanych.__ZNAK_REZYGNACJA:
                    break
                # znaki pozostałe więc powtórz zapytanie
                else:
                    self.komunikat(f"Niepoprawny wybór. Spróbuj ponownie.")
                    continue
            else:
                # wybór poza zakresem - wróć do podmenu Dane ..
                if not element in range(1,9,1):
                    self.komunikat(
                          f"Przepraszam, akceptujemy cyfry od 1 do {self.__indeksow() - 1}, "
                          f"'{ZmianaDanych.__ZNAK_REZYGNACJA}' rezygnacja."
                          )
                    continue
                # odpowiedź jest w zakresie obsługi, więc zapamiętujemy element rekordu
                self.__pozycja_elementu = element
                return True



    def __proceduj_wybor(self) -> bool:

        # wyrejestrowanie się wymaga osobnej ścieżki
        if not self.__pozycja_elementu == 8:

            # odczytujemy wartość elementu przed jego zmianą
            self.__stara_wartosc_elementu = ZmianaDanych.__LST_BAZA[self.__indeks_rekordu][self.__pozycja_elementu]

            # odczytuje nazwę klucza dla zadanej wartości
            nazwa_klucza = list(ZmianaDanych.__INDEKSY_REKORDU.keys())[self.__pozycja_elementu]

            while True:

                # zapytaj o nową wartość
                nowa_wartosc = input(f"\n\tPodaj nowe dane <{nazwa_klucza}>, "
                                     f"'q' rezygnacja: ").strip()
                # rezygnacja
                if nowa_wartosc == ZmianaDanych.__ZNAK_REZYGNACJA:
                    # return False
                    break

                # hasło
                if self.__pozycja_elementu == 6:

                    # powtórz pętlę jeśli są takie same
                    if self.__identyczne(self.__stara_wartosc_elementu, nowa_wartosc):
                        self.komunikat('To jest aktualne hasło - podaj nowe.')
                        continue #return False

                    nowa_wartosc_powtorzona = input(
                                                  f"\n\tPowtórz nowe <haslo>, "
                                                  f"'q' rezygnacja: "
                                                  ).strip()

                    if nowa_wartosc_powtorzona == ZmianaDanych.__ZNAK_REZYGNACJA:
                        return False

                    # powtórz pętlę jeśli niezgodne
                    if not self.__identyczne(nowa_wartosc, nowa_wartosc_powtorzona):
                        self.komunikat('Nowe wartości są różne. Powtórz x2 nowe hasło.')
                        continue

                    # zapisz
                    self.__wartosc_elementu = nowa_wartosc
                    return True

                # zainteresowania - mogą być puste!
                elif self.__pozycja_elementu == 7:
                    self.__wartosc_elementu = nowa_wartosc
                    return True

                # pozostałe dane nie mogą być puste
                else:
                    if not nowa_wartosc:
                        self.komunikat('Brak informacji nie jest akceptowany.')
                        continue

                    if not self.__identyczne(self.__stara_wartosc_elementu, nowa_wartosc):
                        self.__wartosc_elementu = nowa_wartosc
                        return True
                    self.komunikat('Nowe dane powinny różnić się od poprzednich.')
                    continue

        # wyrejestrowanie
        else:
            self.komunikat('.. usuwanie danych w przygotowaniu.', monit=False)
            res = input("Potwierdź, czy napewno chcesz nas opuścić? {tak/nie}: ")
            if res == 'tak':
                x = self.__wyrejestruj()
                if x:
                    self.komunikat('Twoje dane zostały usunięte z ewidencji.', monit=False)
                    # wyjście z pętli
                    return False
                self.komunikat('Jest powód dla którego w tej chwili dane nie mogły być usunięte. Odezwiemy się.', monit=True)
                return False
    #


    def __wyrejestruj(self) -> bool:
        ''' Wykasowanie rekordu i zapisanie go w plik Wyrejestrowani.
        :return: None
        '''
        return umowa.Wypowiedzenie(self.__id).deaktywuj()


    @classmethod
    def __import_bazy(cls):
        with open(cls.__STR_BAZA, 'r') as f:
            lines = f.readlines()
            cls.__LST_BAZA = [(line.strip('\n').split(';')) for line in lines]


    @classmethod
    def __zwroc_nr_rekordu(cls, dla_id: str, kolumna: int = 0) -> int | None:
        ''' Tworzy listę samych ID wyjętych z rekordów z bazy.
        Lista IDs będzie miała dokładnie tę samą długość co baza.
        List.index() zwraca index listy pod którym wystepuje ID.
        :return: numeric, lub None kiedy ID nie występuje.
        '''
        lista = [line[0] for line in cls.__LST_BAZA]
        try:
            return lista.index(dla_id)
        except ValueError:
            return None


    def komunikat(self, jednowiersz, monit: bool = True):
        ''' Komunikat wyświetla jednoliniowe informacje.
        Jeśli argument monit = True, komunikat dodaje tytuł z
        imitacją głośnika, aby wzbudzić większą uwagę usera.
        Jeśli jednowiersz jest pusty, nic nie jest wyświetlane.
        :return: None
        '''
        glosnik: str = '<) '
        jednowiersz = str(jednowiersz).strip()
        if not jednowiersz:
            return None
        if monit:
            tytul = f'{glosnik}Ups..'
            print(f'\n\t{tytul}\n\t{jednowiersz}\n')
        else:
            print(f'\n\t{glosnik}{jednowiersz}\n')



    def __identyczne(self, pierwszy: str, drugi: str) -> bool:
        ''' Zwraca logiczną wartość porównania dwóch argumentów "str" '''
        if isinstance(pierwszy, str) and isinstance(drugi, str):
            return pierwszy == drugi
        return print('Oba argumenty porównania muszą być typu "str"')



    def __zmiana(self) -> bool:
        ''' Zapisuje zmiany w rekordzie. Parametry pobiera z atrybutów instancji.
        :return: 'bool' False / True - kiedy zapis udany.
        '''
        try:
            ZmianaDanych.__LST_BAZA[self.__indeks_rekordu][self.__pozycja_elementu] = self.__wartosc_elementu
            return True
        except Exception:
            return False


    @classmethod
    def __odpowiedz_z_menu(cls) -> str:
        '''
        Menu "Dane .." is displayed and retrive the user's response.
        Menu items are taken from the list data layout template.
        :return: number|text: both formatted as 'str'
        '''
        tekst = f'Menu "Dane czytelnika"'
        linia = f'\n\t{'-' * len(tekst)}'
        tekst = f'\n\t{tekst}'
        tekst += linia
        for key, value in cls.__INDEKSY_REKORDU.items():
            if value in range(1, 9, 1):
                if value == 8:
                    key = 'Wypowiedzenie umowy'
                tekst += f'\n\t{value} = {key}'
        tekst += linia
        tekst += (f"\n\tWybierz 1 do 8, albo '{ZmianaDanych.__ZNAK_REZYGNACJA}'"
                  f"\n\taby wrócić do Menu Głównego: ")
        return input(tekst)


    @classmethod
    def __aktualizacja_bazy_txt(cls):
        with open(cls.__STR_BAZA,'w') as f:
            if isinstance(cls.__LST_BAZA[0], list):
                for i, rekord in enumerate(cls.__LST_BAZA):
                    f.write(';'.join([str(element) for element in rekord]) + '\n')
            else:
                f.write(';'.join([str(element) for element in cls.__LST_BAZA]) + '\n')


# CALL
edycja = ZmianaDanych().edycja_danych_uzytkownika()



