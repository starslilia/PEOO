ossos = input()
reino = input()
alimentacao = input()
if ossos == 'vertebrado':
    if reino == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    if reino == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if reino == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if alimentacao == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
