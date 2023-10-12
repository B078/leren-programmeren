#constanten
DIKTE_TOUW_KLEIN = 3.0
DIKTE_TOUW_MIDDEL = 4.5
DIKTE_TOUW_GROOT = 6.3
PRIJS_PER_METER_KLEIN = 2.75
PRIJS_PER_METER_MIDDEL = 4.60
PRIJS_PER_METER_GROOT = 6.10

import time

print("------prijzenlijst------")
print(f"klein touw  prijs: {DIKTE_TOUW_KLEIN} euro")
print(f"middel touw prijs: {DIKTE_TOUW_MIDDEL} euro")
print(f"groot touw  prijs: {DIKTE_TOUW_GROOT} euro")
print("-----prijzenlijst-------")
print()

#gegevens
while True:
    try:
        aantal_klein_touw = int(input("Hoeveel stukken wilt u van de kleine touw? "))
        lengte_klein_touw = float(input("wat had u gewild als lengte per stuk? (in meters) "))
        print()
        break
    except ValueError:
        print("ongeldige invoer, !!voer alstublieft een geldig getal in!!")

while True:
    try:
        aantal_middel_touw =int(input("Hoeveel stukken wilt u van de middel touw? "))
        lengte_middel_touw = float(input("wat had u gewild als lengte per stuk? (in meters) "))
        print()
        break
    except ValueError:
        print("ongeldige invoer, !!voer alstublieft een geldig getal in!!")

while True:
    try:
        aantal_groot_touw = int(input("Hoeveel stukken wilt u van de grote touw? "))
        lengte_groot_touw = float(input("wat had u gewild als lengte per stuk touw? (in meters) "))
        print()
        break
    except ValueError:
        print("ongeldige invoer, !!voer altstublieft een geldig getal in!!")


#bereking

prijs_touw_klein = (lengte_klein_touw * PRIJS_PER_METER_KLEIN) * aantal_klein_touw
prijs_touw_middel = (lengte_middel_touw * PRIJS_PER_METER_MIDDEL) * aantal_middel_touw
prijs_touw_groot = (lengte_groot_touw * PRIJS_PER_METER_GROOT) * aantal_groot_touw

totaal_prijs = prijs_touw_klein + prijs_touw_middel + prijs_touw_groot

#output
print()
time.sleep(1.5)
print("- - - - - - - - - - - - - - - - - - - - - -  -")
print("bestellingoverzicht: ")
print(f"dikte klein:  {DIKTE_TOUW_KLEIN}, aantal stukken: {aantal_klein_touw}, aantal meters: {lengte_klein_touw}")
print(f"dikte middel: {DIKTE_TOUW_MIDDEL}, aantal stukken: {aantal_middel_touw}, aantal meters: {lengte_middel_touw}")
print(f"dikte groot:  {DIKTE_TOUW_GROOT}, aantal stukken: {aantal_groot_touw}, aantal meters: {lengte_klein_touw}") 
print("- - - - - - - - - - - - - - - - - - - - - - - ")
print(f"uw totaal te betalen bedrag is {totaal_prijs} euro")