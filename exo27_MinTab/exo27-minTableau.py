# Exercice 27
# Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers 
# et qui affiche le plus petit de ces entiers mais cette fois-ci à l'aide
# d'un tableau et sans retenir le minimum lors de la saisie.

array = []


for i in range(10):
    array.append(int(input(f'Entrez le nombre n°{i + 1} : ')))

min = array[0]
max = array[0]

for index, number in enumerate(array):
    if number < min:
        min = number
        index_min = index

    if number > max:
        max = number
        index_max = index

print(array)
print(f'Le minimum du tableau est {min} à la position {index_min}.')
print(f'Le maximum du tableau est {max} à la position {index_max}.')
