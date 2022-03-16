# exo 24 
# Écrivez un algorithme demandant à l’utilisateur 
# le nombre de joueurs (max 10 joueurs) 
# Ensuite, l’algorithme doit demander à l’utilisateur 
# le score de chaque joueur Une fois ceci fini, 
# il faut afficher la moyenne des scores

MAX_NB_PLAYER = 10
array = []

nbPlayers = int(input('Entrez le nombre de joueurs (max 10) : '))

while not 1 <= nbPlayers <= 10:
    print('Vous devez entrer un nombre compris entre 1 et 10.')
    nbPlayers = int(input('Ré-entrez le nombre de joueurs : '))

sum = 0

for i in range(nbPlayers):
    score = int(input('Entrez un score : '))
    array.append(score)
    sum += score

average = sum / nbPlayers

print(array)
print(f'La moyenne des scores est de {average}.')
