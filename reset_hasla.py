from waliduj_login_email import waliduj_login_email
from resetowanie import resetowanie
def reset_hasla(nazwa_pliku):
    
    print("Wpisz 'q' aby wrócić do poprzedniego menu.")

    while True:
        login, email = resetowanie()
        if login != 'q' and email != 'q':
            waliduj_login_email(login, email, nazwa_pliku="baza_uzytkownikow.txt")
            nowe_haslo = input("Prosze podać nowe hasło:")
            nowe_haslo_pow = input('Prosze powtórzyć hasło:')
            if nowe_haslo == nowe_haslo_pow:
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
                break
            else:
                print("Podane hasła róznią się. Spróbuj ponownie.")  
        else:
            print("Błędny login lub email - spróbuj ponownie.")
            break
        