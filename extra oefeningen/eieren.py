DOOS_12 =12
DOOS_10 = 10

aantal_eieren = int(input("Hoeveel eieren moet ik verpakken? "))

#zo min mogelijk en zo klein mogelijk dozen
#stel 13: 1 van 12 en 1 van 6
#stel 25: 2 van 12 en 1 van 6 

#stap 1: hoeveel dozen van 12 (19 -> 7)
dozen_12 = aantal_eieren // DOOS_12
#stap 2: rest uitrekenen(19 ->1)
rest = aantal_eieren - dozen_12 * DOOS_12
#stap 3: hoeveel dozen van 6 (7->1)
dozen_10 = rest // DOOS_10
#stap 4: rest uitreken 7 
rest = rest - dozen_10 * DOOS_10
#stap 5 als ik rest heb 1` extra doos van 6 
if rest >= 1:
    dozen_10 = dozen_10 + 1
    print(f"u heeft {dozen_12} dozen van {DOOS_12} en {dozen_10 } dozen van {DOOS_10}")
    
else:
    print(f"u heeft {dozen_12} dozen van {DOOS_12} en {dozen_10 } dozen van {DOOS_10}")
    

