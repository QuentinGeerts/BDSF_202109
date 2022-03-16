# exo34
# Réalisez une fonction de recherche dans un tableau. 
# Cette fonction va recevoir un tableau, la taille du 
# tableau, et la valeur recherchée en paramètres 
# et renvoyer l’indice de l’élément dans le tableau.
# Si l’élément ne s’y trouve pas, la fonction renvoie -1.

def search_in_array(array, size, searched_value):
    found_index = []
    for i in range(size):
        if array[i] == searched_value:
            found_index.append(i)
    
    return found_index if len(found_index) > 0 else -1


import random

array = []

for i in range(10):
    array.append(random.randint(1, 100))

print(array)
for i in range(5): 

    searched_value = int(input("Entrez une valeur à rechercher : "))

    # Recherche de la valeur dans le tableau
    index = search_in_array(array, len(array), searched_value)

    # Affichage du résultat
    # Si une valeur a été trouvée
    print(f"La value recherchée {searched_value} est à l'index {index}")
