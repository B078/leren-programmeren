
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
time.sleep(0.5)
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

kortingsbonnen = input("Heeft u kortingsbonnen? (ja/nee) ") 
 
if kortingsbonnen == "ja": 
    time.sleep(1)
    print("                                                             ")
    hoeveelheid_kortingsbonnen  = input("Hoeveel kortingbonnen heeft u? ")
    print("---------------------------------")
    time.sleep(0.5)
    prijs_per_kortingsbon = float(input("Wat is de waarde van de bonnen? "))
    korting = float(hoeveelheid_kortingsbonnen) * float(prijs_per_kortingsbon)
    time.sleep(1.5)
    print("    ")
    print("Uw korting is", korting ,"euro" )

     #bereking
    prijs_croissanten = prijs_per_croissant * aantal_croissantjes
    prijs_stokbroden = prijs_per_stokbrood * aantal_stokbroden

    totaal = (prijs_croissanten + prijs_per_stokbrood) - korting
    time.sleep(1)
    print(" ")
    print("|-------------------------------------------------------------|")
    print("|                                                             |")
    print("| Het bedrag wordt uitgerekend, een moment geduld alstublieft.|")
    print("|                                                             |")
    print("|-------------------------------------------------------------|")
    time.sleep(5)

    print(" ")
    print(f"Uw te betalen bedrag is {round(totaal, 2 )} euro")
    print("----------------------------------")

elif kortingsbonnen == "nee":
    #berekening 
    prijs_croissanten = prijs_per_croissant * aantal_croissantjes
    prijs_stokbroden = prijs_per_stokbrood * aantal_stokbroden

    totaal = prijs_croissanten + prijs_stokbroden
    time.sleep(1)
    print(" ")
    print("|------------------------------------------------------------|")
    print("|                                                            |")
    print("| Uw bedrag wordt uitgerekend, een moment geduld alstublieft.|")
    print("|                                                            |")
    print("|------------------------------------------------------------|")
    time.sleep(5)
    print(" ")
    print(f"Het te betalen bedrag is, {round(totaal, 2)} euro")
    print("------------------------------------")

else: 
     print("   ")
     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
     print("Dit kan ik niet verwerken! ")
     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
     print("type (ja) of (nee) alstublieft!")
     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
     print("   ")