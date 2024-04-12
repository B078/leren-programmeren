eieren = ['roze', 'geel', 'groen', 'rood', 'blauw']
plekken = [9, 0, 4, 6, 3, 9, 10, 7, -1, -70]
lege_plekken = []

for plek in plekken:
    if plek >= 0 and plek < len(eieren):
        print(f"Bij de {plek}e plek is het {eieren[plek]} ei gevonden")
    else:
        lege_plekken.append(plek)

print("Lege plekken:", lege_plekken)
