# exo 19 
# À l’aide de la boucle TANTQUE FAIRE, réalisez un algorithme calculant 
# le résultat de N 10
# N étant un nombre saisi par l’utilisateur

number = int(input('Entrez un nombre : '))
count = 0
exponant = 10
result = 1

while count < exponant:
    result *= number
    count += 1

print(number, 'exp', exponant, '=', result)

# ---------------------------------------------

number = int(input('Entrez un nombre : '))

exponant = 10 
result = number ** exponant
print(number, 'exp', exponant, '=', result)

# ---------------------------------------------

import math

result = math.pow(2, 10)
print(result)
