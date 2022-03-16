# exo 26 
# À l’aide des boucles, réalisez un algorithme permettant
# de trier un tableau d’entiers dans l’ordre croissant 
# Mettez le ensuite en pratique avec le Python


array = [8, 9, 5,4, 5, 1,  1, 2] # [2, 1, 5, 9, 8]

# -- Méthodes algo python --

for i in range(0, len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            # array[i], array[j] = array[j], array[i]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            
print(array)

# -- Méthode python --
array.sort()
print(array)
