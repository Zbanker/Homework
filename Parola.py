parola = 'pixel700'
try1 = input('Introduceti parola (3 incercari): ')

if try1 != parola:
    try2 = input('Parola gresita incercati din nou (2 incercari):\n ')
    if try2 != parola:
        try3 = input('Parola gresita incercati din nou (1 incercari):\n ')
        if try3 != parola:
            print('Cont blocat')
        else:
            print('Acces permis')
    else:
        print('Acces permis')
else:
    print('Acces permis')