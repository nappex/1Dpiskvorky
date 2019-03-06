def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka)
        odpoved = odpoved.lower().strip()
        print(odpoved, len(odpoved))
        if odpoved == ("a" or "ano"):
            return True
        elif odpoved == ("n" or "ne"):
            return False
        else:
            print('Nerozumím! Odpověz "ano/ne" nebo "a/n".')


if ano_nebo_ne("Chceš si zahrát hru? "):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
