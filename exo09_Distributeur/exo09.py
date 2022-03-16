# exo09 Distributeur de boissons (Pseudo Code + Python)
# Réalisez l’algorithme d’un distributeur de boissons. 
# Ce dernier propose plusieurs boissons et l’utilisateur 
# choisit celle qu’il  désire en entrant le numéro correspondant. 
# N'oubliez pas de vérifier s’il y a encore des boissons en stock.

# Initialisation du stock de boisson
stockEau = 2
stockCoca = 0
stockFanta = 1

# Proposition des boissons
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
