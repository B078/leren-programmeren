#Je wilt 17 croissantjes van elk 39 eurocent 
#2 stokbroden van elk 2,78 euro kopen. 
#Je hebt 3 kortingsbonnen van 50 eurocent. Hoeveel geld moet je betalen?

#Maak een programma feestlunch.py voor deze berekening.

import time

# prijs per stuk 
prijs_per_croissant = 0.39 
prijs_per_stokbrood = 2.78

print("goedemiddag mevrouw. ")
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
    waarde_korting = int(input("Wat is de waarde van de bonnen "))

hoeveel_korting = waarde_korting * aantal_kortingsbonnen # berekening

print(hoeveel_korting)


                            






#berekening 
kosten_croissanten = aantal_croissantjes * prijs_per_croissant

kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood


