# exo0
# Réalisez un algorithme convertisseur de secondes. Ce dernier reçoit un
# nombre de secondes et détermine le nombre de jours, heures, minutes et
# secondes auquel il correspond.
# Exemple :
# 4561 secondes correspondent à 0 jour 1 heure 16 minutes et 1 seconde.
# Réfléchissez à la méthode que nous devons utiliser.
# Une fois l’algorithme réalisé, testez-le en Python.

# Déclaration des constantes
SEC_IN_DAY = 86400
SEC_IN_HOUR = 3600
SEC_IN_MINUTE = 60

# Demander à l'utilisateur de rentrer un nombre de secondes à convertir
secondsToConvert = int(input("Entrez un nombre de secondes à convertir : "))

# Conversion
day = secondsToConvert // SEC_IN_DAY
hour = (secondsToConvert % SEC_IN_DAY) // SEC_IN_HOUR
minute = ((secondsToConvert % SEC_IN_DAY) % SEC_IN_HOUR) // SEC_IN_MINUTE
second = ((secondsToConvert % SEC_IN_DAY) % SEC_IN_HOUR) % SEC_IN_MINUTE

# Affichage
print(secondsToConvert , " secondes vaut " , day , " jour(s) " , hour ,
       " heure(s) " , minute , " minute(s) " , second , " seconde(s).", sep="")
