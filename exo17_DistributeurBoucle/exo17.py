# exo 17 
# À l’aide d’une boucle FAIRE TANTQUE, améliorez l’algorithme du distributeur 
# de boissons pour qu’il demande au client s’il désire une autre boisson 
# (Tant qu’il en a envie)

# Initialisation du stock de boisson
stockEau = 2
stockCoca = 0
stockFanta = 1

envie = True

while envie:
    # Code à répéter

    print('Stock : ')
    print('Eau : ', stockEau)
    print('Coca : ', stockCoca)
    print('Fanta : ', stockFanta)

    # Proposition des boissons
    print('\nMenu:')
    print("1. Eau, 2. Coca, 3. Fanta")

    # Récupération du choix de l'utilisateur
    choix = int(input("Choix : "))

    # Vérification du choix de l'utilisateur
    # choix >= 0 and choix <= 3
    if 0 < choix <= 3:
        # Choix connu
        print('Choix connu')

        # Vérification du choix de la boisson
        if choix == 1 and stockEau > 0:
            # Eau
            # stockEau = stockEau - 1
            stockEau -= 1
            print('Merci pour votre achat')

        elif choix == 2 and stockCoca > 0:
            stockCoca -= 1
            print('Merci pour votre achat')

        elif choix == 3 and stockFanta > 0:
            stockFanta -= 1
            print('Merci pour votre achat')

        else:
            print("Hors stock")

    else :
        # Choix inconnu
        print('Choix inconnu')


    envie = input('Voulez-vous une autre boisson ? oui / non : ') == 'oui'
