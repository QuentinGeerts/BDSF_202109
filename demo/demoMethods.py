# Procédures
# Sans paramètre
def direBonjour():
    print('Bonjour')

# Avec paramètre(s)
def direBonjourPrenom(prenom):
    prenom = "Menen"
    print(f'Bonjour {prenom}')

# Fonctions
def multiplierPar2(nb):
    return nb * 2

# --- Programme ---
# direBonjour()
direBonjourPrenom("Quentin")
prenom = "Seb"
print(prenom) # "Seb"
direBonjourPrenom(prenom) # Bonjour Menen
print(prenom) # "Seb"

print(multiplierPar2(2))

result = multiplierPar2(25)

print(result)


# définition de la fonction
def metajour (tab):
    tab[0] = 3
tableau = [0, 1]
#appel de la fonction
print(tableau)
metajour(tableau)
print(tableau)