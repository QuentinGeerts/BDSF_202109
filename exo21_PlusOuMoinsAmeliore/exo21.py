# exo 21 
# Améliorez le "C'est plus, c'est moins, c'est gagné" pour qu'il 
# tourne en boucle tant que le justePrix n'a pas été trouvé

# L'ordinateur choisit un nombre aléatoirement entre 1 et 100
# L'utilisateur est invité à entrer un nombre et l'algorithme 
# nous répond "C'est plus" ou "C'est moins"

# Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre
# de tentatives effectuées pour trouver le résultat

from random import randint

just_price = randint(1, 100)

isFound = False
count = 0

while not isFound:
    proposal = int(input('Entrez un nombre : '))
    count += 1

    if proposal == just_price:
        isFound = True
   
    elif proposal < just_price:
        print('C\'est plus')

    else:
        print('C\'est moins')


print(f'C\'est gagné en {count} essai(s)')