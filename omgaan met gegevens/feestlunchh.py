
#prijs per stuk
prijs_croissant = 0.39
prijs_stokbrood = 2.78

#aantallen
aantal_croissant = 17
aantal_stokbroden = 2

kortings_bonnen = 3
waarde_bonnen = 0.50 

#berekening

prijzen_croissant = aantal_croissant * prijs_croissant
prijzen_stokbroden = aantal_stokbroden * prijs_stokbrood
aantal_korting = kortings_bonnen * waarde_bonnen

totaal = prijzen_croissant + prijzen_stokbroden - aantal_korting

#resultaat
print(" ")
print(f"De feestlunch kost je bij de bakker {round(totaal, 2 )} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")