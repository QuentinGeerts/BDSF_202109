pret = input("Êtes-vous prêt ? oui / non ").lower() == 'oui'
panier_vide = input('Le panier est-il vide ? oui / non ').lower() == 'oui'

if pret and not panier_vide :
    # bloc d'instructions
    print('Lancer la balle')
else:
    print('Ne pas lancer la balle')

    if not pret : 
        print('Car vous n\'êtes pas prêt.')
    
    if panier_vide : 
        print('Car le panier est vide.')