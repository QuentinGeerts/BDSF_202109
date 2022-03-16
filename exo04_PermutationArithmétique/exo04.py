# exo04-Bonus : Imaginez une méthode permettant d’inverser le contenu d’une variable entière SANS utiliser une variable temporaire.

# Déclaration
nb1 = 5
nb2 = 7

# Affichage
print(nb1, nb2, sep="\n")

# Traitement
nb1 = nb1 + nb2 # 5 + 7 = 12
nb2 = nb1 - nb2 # 12 - 7 = 5
nb1 = nb1 - nb2 # 12 - 5 = 7

# nb1 = nb1 * nb2
# nb2 = nb1 / nb2
# nb1 = nb1 / nb2 



# Affichage
print(nb1, nb2, sep="\n")