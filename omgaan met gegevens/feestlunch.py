#Je wilt 17 croissantjes van elk 39 eurocent 
#2 stokbroden van elk 2,78 euro kopen. 
#Je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen?

#Maak een programma feestlunch.py voor deze berekening.

# prijs per stuk 
prijs_per_croissant = 0.39 
prijs_per_stokbrood = 2.78

import time

print("goedemiddag. ")
time.sleep(1.5)

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

aantal_kortingsbonnen = input("Heeft u kortingsbonnen? (j/n) ")
 
if aantal_kortingsbonnen == "j": 
    hoeveelheid_kortingsbonnen  = input("Hoeveel kortingbonnen heeft u? ")
    print("                               ")
    prijs_per_kortingsbon = float(input("Wat is de waarde van de bonnen "))
    korting = float(hoeveelheid_kortingsbonnen) * float(prijs_per_kortingsbon)
    print(korting)


#berekening 
kosten_croissanten = aantal_croissantjes * prijs_per_croissant

kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood


