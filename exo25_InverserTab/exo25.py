# exo 25
# Inversez un tableau soit un tableau T Saisissez ce tableau 
# Changez de place les éléments de ce tableau de façon à ce 
# que le nouveau tableau soit une sorte de miroir de l'ancien 
# et affichez le nouveau tableau

array = [8, 9, 5, 4, 5, 1,  1, 2] # [2, 1, 5, 9, 8]
array2 = []
# -- Méthodes algo python --

for i in range(len(array)-1, 0, -1):
    array2.append(array[i])

print(array2)

# -- Méthode python --

# array2 = array[:]
# array2.reverse()

# array2 = array[::-1]

# print(array2)
