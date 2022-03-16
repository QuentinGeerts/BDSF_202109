# exo 15 À l’aide de deux boucles, affichez 
# les tables de multiplication de 1 à 9

# Initialisation 1
table = 1

# Condition 1
while table <= 9:

    print('La table de multiplication de', table)

    # Initilisation 2 
    number = 1

    # Condition 2
    while number <= 10:
        print(number, '*', table, '=', number * table)

        # Incrémentation 2
        number += 1
    
    # Incrémentation 1
    table += 1
