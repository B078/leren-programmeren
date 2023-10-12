# Vraag de gebruiker om twee gehele getallen in te voeren
while True:
    try:
        a = int(input("Voer het eerste gehele getal (a) in: "))
        break
    except ValueError:
        print("invoer ongeldig, voer een geheel getal in alstublieft!")
        
while True:
    try:
        b = int(input("Voer het tweede gehele getal (b) in: "))
        break
    except ValueError:
        print("invoer ongeldig, voer een geheel getal in alstublieft!")

#varabile
MIN = a
MAX = a

# Controleer of a groter is dan b
if a > b:
    Max = a
    print("a is het grootste getal:", Max)
# Controleer of a kleiner is dan b
elif a < b:
    Min = a
    print("a is het kleinste getal:", Min)
#controleer of a gelijk is aan b
else:
    print("a en b zijn even groot.")

print("het minimum is:", MIN)
print("het maximium is", MAX)
    

