# exo10 Calculatrice (Pseudo Code + Python)
# Réalisez l’algorithme d’une calculatrice basique.
# L’utilisateur est invité à saisir un nombre, un opérateur et un deuxième nombre.
# La calculatrice affiche ensuite le calcul et le résultat.
# (Gérer la division par 0)

nb1 = float(input('Entrez le premier nombre : '))           # 22.2
operator = input('Entrez l\'opérateur (+, -, *, /, //): ')  # /
nb2 = float(input('Entrez le deuxième nombre : '))          # 3.2

if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "//":
    print("Opérateur reconnu")

    if operator == "+":
        # Addition
        result = nb1 + nb2

    elif operator == "-":
        # Soustraction
        result = nb1 - nb2

    elif operator == "-":
        # Multiplication
        result = nb1 * nb2

    elif operator == "/":
        # Division
        if nb2 != 0:
            result = nb1 / nb2

    elif operator == "//":
        # Division entière
        if nb2 != 0:
            result = nb1 // nb2

    # Affichage
    if (operator == "/" or operator == "//") and nb2 == 0:
        print('Division par 0 impossible')
    else:
        print(nb1, operator, nb2, "=", result)

else:
    print("Opérateur non reconnu")
