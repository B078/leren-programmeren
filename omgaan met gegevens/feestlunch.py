import time

# prijs per stuk 
PRIJS_PER_CROISSANT = 0.39 
PRIJS_PER_STOKBROOD = 2.78


print("Welkom bij Bakker Verschoor ")
print(" ")
time.sleep(1)

print("---------PRIJZEN LIJST-----------")
print("1 croissantje kost," ,PRIJS_PER_CROISSANT)
print("1 stokbroodje kost," , PRIJS_PER_STOKBROOD)
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
    prijs_croissanten = PRIJS_PER_CROISSANT * aantal_croissantjes
    prijs_stokbroden = PRIJS_PER_STOKBROOD * aantal_stokbroden

    totaal = (prijs_croissanten + prijs_stokbroden) - korting
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
    prijs_croissanten = PRIJS_PER_CROISSANT * aantal_croissantjes
    prijs_stokbroden = PRIJS_PER_STOKBROOD* aantal_stokbroden

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