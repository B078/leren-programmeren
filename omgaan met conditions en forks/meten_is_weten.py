# Vraag de gebruiker om twee gehele getallen in te voeren
while True:
    try:
        a = int(input("Voer het eerste gehele getal (a) in: "))
        break
    except ValueError:
        print("Invoer ongeldig, voer een geheel getal in alstublieft!")
        
while True:
    try:
        b = int(input("Voer het tweede gehele getal (b) in: "))
        break
    except ValueError:
        print("Invoer ongeldig, voer een geheel getal in alstublieft!")

# Variabelen
min_value = a
max_value = a

# Controleer of a groter is dan b
if a > b:
    max_value = a
    min_value = b
    print("a is het grootste getal:", max_value)
# Controleer of a kleiner is dan b
elif a < b:
    min_value = a
    max_value = b
    print("a is het kleinste getal:", min_value)
# Controleer of a gelijk is aan b
else:
    print("a en b zijn even groot.")

print("Het minimum is:", min_value)
print("Het maximum is:", max_value)
