#Je wilt 17 croissantjes van elk 39 eurocent 
#2 stokbroden van elk 2,78 euro kopen. 
#Je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen?

#Maak een programma feestlunch.py voor deze berekening.

# prijs per stuk 
prijs_per_croissant = 0.39 
prijs_per_stokbrood = 2.78

import time

print("Welkom bij Bakker Verschoor ")
print(" ")
time.sleep(1)

print("---------PRIJZEN LIJST-----------")
print("1 croissantje kost," ,prijs_per_croissant)
print("1 stokbroodje kost," , prijs_per_stokbrood)
print("---------PRIJZEN LIJST-----------")
time.sleep(1.5)

print("   ")
print("Goedemiddag.")
print("   ")
aantal_croissantjes = int(input("Hoeveel croissantjes zou u hebben gewild? ")) #hoeveelheden

print("                                   ")
print("Een moment geduld wordt genoteerd. ")
print("                                   ")
time.sleep(1.5)

aantal_stokbroden = int(input("Hoeveel stokbroden had u gewild? ")) #hoeveelheden

print("                                   ")
print("Een moment geduld wordt genoteerd. ")
print("                                   ")
time.sleep(1.5)

kortingsbonnen = input("Heeft u kortingsbonnen? (j/n) ")
 
if kortingsbonnen == "j": 
    time.sleep(1)
    print("                                                             ")
    hoeveelheid_kortingsbonnen  = input("Hoeveel kortingbonnen heeft u? ")
    print("    ")
    print("---------------------------------")
    prijs_per_kortingsbon = float(input("Wat is de waarde van de bonnen "))
    korting = float(hoeveelheid_kortingsbonnen) * float(prijs_per_kortingsbon)
    print("    ")
    print("Uw korting is", korting ,"euro" )

     #bereking
    prijs_croissanten = prijs_per_croissant * aantal_croissantjes
    prijs_stokbroden = prijs_per_stokbrood * aantal_stokbroden

    totaal = (prijs_croissanten + prijs_per_stokbrood) - korting
    time.sleep(1)
    print(" ")
    print("----------------------------------|")
    print(f"Het te betalen bedrag is,{totaal}     |")
    print("----------------------------------|")

elif kortingsbonnen == "n":

    prijs_croissanten = prijs_per_croissant * aantal_croissantjes
    prijs_stokbroden = prijs_per_stokbrood * aantal_stokbroden

    totaal = prijs_croissanten + prijs_per_stokbrood
    time.sleep(1)
    print(" ")
    print("-----------------------------------|")
    print(f"Het te betalen bedrag is, {totaal}    |")
    print("-----------------------------------|")

else: 
    kortingsbonnen != "n" and kortingsbonnen != "j"; 
print("Dit kan ik niet verwerken! ")


