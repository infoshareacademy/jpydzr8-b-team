from waliduj_login_email import waliduj_login_email



def reset_hasla(nazwa_pliku) -> bool:
    '''
    Za każdym razem kiedy użytkownik rezygnuje,
    funkcja zwraca False co znaczy, że reset
    hasła nie został przeprowadzony.
    :return: bool
    '''
    zgodnosc: bool = False

    print("Zawsze możesz zrezygnować i wrócić do Menu - 'q'")

    while True:

        # zabezpiecz przed powtórnym pytaniem skoro
        # już raz zweryfikowano poprawność danych
        if not zgodnosc:
            login, email = __pobrane_do_weryfikacji()
            if 'q' in (login, email):
                break
            zgodnosc = waliduj_login_email(login, email, nazwa_pliku="baza_uzytkownikow.txt")
            if not zgodnosc:
                print("Błędny login lub email - spróbuj ponownie.")
                continue

        nowe_haslo = input("Teraz podaj nowe hasło: ")
        nowe_haslo_pow = input('Powtórz nowe hasło: ')
        if 'q' in (nowe_haslo, nowe_haslo_pow):
            break

        if nowe_haslo != nowe_haslo_pow:
            print("Hasła różnią się. Spróbuj ponownie.")
            continue

        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            linie = plik.readlines()
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            for linia in linie:
                dane = linia.strip().split(';')
                if len(dane) >= 7 and dane[5] == login and dane[4] == email:
                    dane[6] = nowe_haslo
                    linia = ';'.join(dane) + '\n'
                else:
                    linia = ';'.join(dane) + '\n'
                plik.write(linia)
        print("Hasło zostało zresetowane pomyślnie.")
        return True


def __pobrane_do_weryfikacji() -> tuple[str | None, str | None]:
    '''Zwraca w 2-elementowej krotce pobrane dane do weryfikacji,
    albo 'q' - rezygnację z resetu.'''
    a = True
    login = None
    email = None
    while a:
        login = input("WER Proszę podać login: ")
        if login == 'q':
            break
        email = input("WER Proszę podać email: ")
        if email == 'q':
            break
        a = False
    return login, email