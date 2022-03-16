# Exercice 28
# Réalisez un algorithme permettant de rechercher une 
# valeur dans un tableau. Si la valeur se trouve
# bien dans le tableau, nous affichons sa position.
import random

array = []
found_index = []

for i in range(10):
    array.append(random.randint(1, 100))

print(array)

search_value = int(input("Entrez une valeur à rechercher : "))

# Recherche de la valeur dans le tableau
for index, value in enumerate(array):
    if value == search_value:
        found_index.append(index)

# Affichage du résultat
# Si une valeur a été trouvée
if len(found_index) != 0:
    print(f'La valeur {search_value} a été trouvée', end="")
    if len(found_index) > 1: print(f' aux index {found_index}')
    else : print(f' à l\'index {found_index[0]}')
# Sinon
else :
    print(f"Aucune valeur trouvée dans le tableau pour la valeur {search_value}.")