# exo 14 
# Reprenez l’algorithme du lanceur de balles de tennis 
# et faites en sorte qu’il lance une balle tant que le 
# stock n’est pas vide Il y a donc 2 variables stockBalles 
# et pret

stock_balles = int(input("Combien de balles avez-vous ?"))

while stock_balles > 0:
    print(f"Il vous reste {stock_balles} balle(s) à lancer")
    pret = bool(int(input("Êtes-vous prêt : 1 = oui / 0 = non")))

    if pret :
        print('Lancer la balle')
        stock_balles -= 1
    else :
        print('Ne pas lancer la balle')

print('Il n\'y a plus de balles, partie terminée.')
