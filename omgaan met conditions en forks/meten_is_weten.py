# Vraag de gebruiker om het eerste gehele getal (a) in te voeren
while True:
    try:
        a = int(input("Voer het eerste gehele getal (a) in: "))
        break
    except ValueError:
        print("Ongeldige invoer voor a. Voer een geheel getal in alstublieft!")

# Vraag de gebruiker om het tweede gehele getal (b) in te voeren
while True:
    try:
        b = int(input("Voer het tweede gehele getal (b) in: "))
        break
    except ValueError:
        print("Ongeldige invoer voor b. Voer een geheel getal in alstublieft!")

# Variabelen voor minimum en maximum
MIN = a
MAX = a

# Controleer of a groter is dan b
if a > b:
    MAX = a
    print("a is het grootste getal:", MAX)
# Controleer of a kleiner is dan b
elif a < b:
    MIN = a
    print("a is het kleinste getal:", MIN)
# Controleer of a en b gelijk zijn
else:
    print("a en b zijn even groot.")

print("Het minimum is:", MIN)
print("Het maximum is:", MAX)
