# exo 16
# Un algorithme reçoit deux nombres de l’utilisateur : justePrix et proposition
# Il répond « C’est plus »
#   lorsque proposition est plus petit que justePrix
# Il répond « C’est moins »
#   lorsque proposition est plus grand que justePrix
# Si justePrix est égal à proposition, il répond « C’est gagné »

# juste_prix = int(input('Entrez un juste prix : '))

# proposition = int(input('Entrez une proposition : '))

# while juste_prix != proposition:

#     if proposition < juste_prix:
#         print('C\'est plus')
#     else:
#         print('C\'est moins')

#     proposition = int(input('Entrez une proposition : '))

# print('C\'est gagné')

# -------------------

juste_prix = int(input('Entrez un juste prix : '))

estTrouve = False

while not estTrouve:
    proposition = int(input('Entrez une proposition : '))

    if proposition < juste_prix:
        print('C\'est plus')
    elif proposition == juste_prix:
        estTrouve = True
    else:
        print('C\'est moins')

print('C\'est gagné')
