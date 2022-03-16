# exo 22 
# Écrivez un algorithme qui saisit 6 entiers et les stocke dans 
# un tableau, puis affiche le contenu de ce tableau une fois 
# qu’il est rempli

print('Première méthode')
array = [0] * 6
index = 0

# Remplissage du tableau
while index < len(array):
    nb = int(input("Entrez une nombre : "))
    array[index] = nb
    # array[index] = int(input("Entrez une nombre : "))
    index += 1

# Affichage du tableau
print(array)

# -------------------------------

print('Deuxième méthode')
array = []
index = 0
LENGTH = 6

# Remplissage du tableau
while index < LENGTH:
    nb = int(input("Entrez une nombre : "))
    array.append(nb)
    index += 1

# Affichage du tableau
print(array)

# -----------------------

