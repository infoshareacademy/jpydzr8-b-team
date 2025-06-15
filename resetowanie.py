def resetowanie() -> tuple[str | None, str | None]:

    a = True
    login = None
    email = None
    while a:
        login = input("RESETOWANIE Prosze podać login: ")
        if login == 'q':
            a = False
        email = input("RESETOWANIE Proszę podać email: ")
        if email == 'q':
            a = False
    return(login, email)