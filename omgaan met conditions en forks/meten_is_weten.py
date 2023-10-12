# Vraag de gebruiker om twee gehele getallen in te voeren
a = float(input("Voer het eerste gehele getal (a) in: "))
b = float(input("Voer het tweede gehele getal (b) in: "))

min = a
max = a

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

print("het minimum is:", min)
print("het maximium is", max)
    

