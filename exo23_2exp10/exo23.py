# exo 23
# BONUS initialisez un tableau de 10 entiers avec les valeurs
# 2 4 8 16 32 64 128 256 512 1024 à l’aide d’une boucle.
# Ensuite, à l’aide d’une boucle affichez la valeur de chaque
# cellule du tableau.

array = []
i = 0

while i < 10:
    array.append(2**(i+1))
    i += 1
# i = 10

i = 0
while i < 10:
    print(array[i])
    i += 1
