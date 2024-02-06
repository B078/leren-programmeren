from garage import autolijst

print(f"Ik heb {len(autolijst)} auto's in mijn garage")

aantal_audi = 0

for auto in autolijst:
    if auto["merk"] == "Audi":
        aantal_audi += 1 

print(f"Ik heb {aantal_audi} Audi's in mijn garage")


lijst = [17,12,15, 15, 2, 8]

print(min(lijst))

min_auto = max(autolijst, key=lambda x: x["motorinhoud"])

print(min_auto)

max_merk = max(autolijst, key=lambda x: len(x["model"]))

print(max_merk)
