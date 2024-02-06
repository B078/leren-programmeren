import random


kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

aantal_mm = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))


zak_mm = {}
for _ in range(aantal_mm):
    kleur = random.choice(kleuren)
    zak_mm[kleur] = zak_mm.get(kleur, 0) + 1


print("De zak met M&M's:")
for kleur, hoeveelheid in zak_mm.items():
    print(f"{kleur}: {hoeveelheid}")
