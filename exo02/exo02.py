# exo02-Récupérez le nom et le prénom de 
# l'utilisateur puis affichez le message 
# "Bienvenue prenom nom"
# Ex : Bienvenue Jules César

# Récupération du nom et du prénom grâce à input
# input retourne un str => chaine de caractères
# Un message peut être indiqué pour préciser ce que l'utilisateur doit entrer
nom = input("Quel est votre nom : ")
prenom = input('Quel est votre prénom : ')

# Affichage formaté du nom et prénom
print(f'Bienvenue {nom} {prenom}')
