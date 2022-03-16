year = int(input("Entrez une année à évaluer : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 : 
    print(f"L'année {year} est bissextile")
else : 
    print(f"L'année {year} n'est pas bissextile")