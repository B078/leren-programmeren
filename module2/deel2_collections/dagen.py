# Tuple met dagen van de week
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Normale volgorde:")
print(" ".join(dagen_van_de_week))

print("\nWerkdagen:")
print(" ".join(dagen_van_de_week[:5]))

print("\nWeekenddagen:")
print(" ".join(dagen_van_de_week[-2:]))

print("\nOmgekeerde volgorde:")
print(" ".join(reversed(dagen_van_de_week)))

print("\nWerkdagen in omgekeerde volgorde:")
print(" ".join(reversed(dagen_van_de_week[:5])))

print("\nWeekenddagen in omgekeerde volgorde:")
print(" ".join(reversed(dagen_van_de_week[-2:])))
