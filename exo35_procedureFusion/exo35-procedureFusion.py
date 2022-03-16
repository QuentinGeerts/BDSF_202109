# exo35
# Réalisez une procédure dont l’objectif est de 
# fusionner deux tableaux d’entiers

def fusion_tab(tab1, tab2):
    # tab = []

    # for value in tab1:
    #     tab.append(value)
    # for value in tab2:
    #     tab.append(value)

    # return tab

    # -----------------------

    # tab = tab1[:]
    # tab.extend(tab2)
    return tab1[:] + tab2[:]

ints1 = [1, 2, 3]
ints2 = [4, 5, 6]

ints3 = fusion_tab(ints1, ints2)

print(ints1)
print(ints2)
print(ints3)
