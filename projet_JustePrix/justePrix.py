# Projet : justePrix
# Améliorez encore le justePrix : l'utilisateur a droit à 10 essais 
# après ces 10 essais, il a perdu et l'ordinateur affiche le justePrix

# Ajouter un niveau :
# - facile : entre 1 et 10
# - moyen : entre 1 et 100
# - difficile : entre 1 et 1000

# Tant que la personne veut rejouer, redemandez le niveau et 
# générez un nombre.
# Vérifiez que tout caractère entré est correct, c'est à dire 
# pour que le programme ne plante jamais.

import random

replay = True
MAX_NB_TRY = 10

easy_level = 'facile : entre 1 et 10'
medium_level = 'moyen : entre 1 et 100'
hard_level = 'difficile : entre 1 et 1000'

while replay:

    # Proposition du menu
    print(f'1. {easy_level}')
    print(f'2. {medium_level}')
    print(f'3. {hard_level}')

    choice = input('Entrez votre choix : ')

    # Vérifier le choix de l'utilisateur
    while not (choice == '1' or choice == '2' or choice == '3'):
        print(f'Le choix ({choice}) n\'est pas correct.')
        choice = input('Entrez votre nouveau choix : ')

    # Choix correct
    # Selectionner le niveau
    if choice == '1':
        print(easy_level)
        selected_level = 10

    elif choice == '2':
        print(medium_level)
        selected_level = 100

    elif choice == '3':
        print(hard_level)
        selected_level = 1000

    # Générer le nombre aléatoire
    just_price = random.randint(1, selected_level)

    isFound = False
    count = 0

    while not isFound and count < MAX_NB_TRY:
        proposal = input(f'{count + 1}. Entrez un nombre : ')
        while not proposal.isdigit():
            proposal = input('Ceci n\'est pas un nombre, réessayez : ')
        count += 1

        proposal = int(proposal)

        if proposal == just_price:
            isFound = True
    
        elif proposal < just_price:
            print('C\'est plus')

        else:
            print('C\'est moins')

    if isFound:
        print(f'C\'est gagné en {count} essai(s) / {MAX_NB_TRY}')
    else:
        print(f'C\'est perdu. Vous avez utilisé vos {MAX_NB_TRY} essais.')
        print(f'Le juste prix a trouvé était {just_price}.')

        

    # Demander à l'utilisateur s'il veut rejouer
    replay = input('Voulez-vous rejouer ? oui / non : ').lower() == 'oui'