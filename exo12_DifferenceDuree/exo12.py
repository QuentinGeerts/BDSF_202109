# exo 12 
# Réalisez un algorithme utilisant le convertisseur de secondes, 
# il reçoit deux durées en jours, heures, minutes et secondes 
# puis il calcule la différence entre ces dernières

SEC_IN_DAY = 86400
SEC_IN_HOUR = 3600
SEC_IN_MINUTE = 60

# j1 = int(input('Entrez la première durée (jour) : '))
# h1 = int(input('Entrez la première durée (heure) : '))
# m1 = int(input('Entrez la première durée (minute) : '))
# s1 = int(input('Entrez la première durée (seconde) : '))

# j2 = int(input('Entrez la deuxième durée (jour) : '))
# h2 = int(input('Entrez la deuxième durée (heure) : '))
# m2 = int(input('Entrez la deuxième durée (minute) : '))
# s2 = int(input('Entrez la deuxième durée (seconde) : '))

j1, h1, m1, s1 = (int(number) for number in input("Entrez la première durée (j h m s) :").split(' ')) # 1 0 0 0
j2, h2, m2, s2 = (int(number) for number in input("Entrez la deuxième durée (j h m s) :").split(' ')) # 1 0 0 0

# Conversion des durées en secondes
t1 = j1 * SEC_IN_DAY + h1 * SEC_IN_HOUR + m1 * SEC_IN_MINUTE + s1
t2 = j2 * SEC_IN_DAY + h2 * SEC_IN_HOUR + m2 * SEC_IN_MINUTE + s2

# Différence entre les deux durées
tT = abs(t1 - t2)

# Reconvertir les secondes en durée
jT = tT // SEC_IN_DAY
hT = (tT % SEC_IN_DAY) // SEC_IN_HOUR
mT = ((tT % SEC_IN_DAY) % SEC_IN_HOUR) // SEC_IN_MINUTE
sT = ((tT % SEC_IN_DAY) % SEC_IN_HOUR) % SEC_IN_MINUTE

# Affichage
print("La durée 1 : " , j1 , ":" , h1 , ":" , m1 , ":" , s1, sep="")
print("La durée 2 : " , j2 , ":" , h2 , ":" , m2 , ":" , s2, sep="")
print("La différence entre les deux durées est de : " , jT , ":" , hT , ":" , mT , ":" , sT, sep="")
