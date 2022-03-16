# exo 20 
# Reprenez l’exercice précédent et modifiez le pour que l’utilisateur
#  entre également l’exposant qu’il désire calculer

number = int(input('Entrez un nombre : '))
count = 0
exponant = int(input('Entrez un exposant : '))
result = 1

while count < exponant:
    result *= number
    count += 1

print(number, 'exp', exponant, '=', result)
