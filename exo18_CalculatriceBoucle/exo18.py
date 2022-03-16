# exo 18 
# À l’aide d’une boucle FAIRE TANTQUE, améliorez l’algorithme de la 
# calculatrice afin qu’elle demande à l’utilisateur s’il veut faire 
# un autre calcul (tant qu’il le désire)

envie = True

while envie:

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


    envie = input('Voulez-vous refaire un autre calcul ? oui / non : ') == 'oui'
