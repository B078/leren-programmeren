
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

totaal_kosten_zonder_korting = prijzen_croissant + prijzen_stokbroden
aantal_korting = kortings_bonnen * waarde_bonnen

totaal_met_korting = prijzen_croissant + prijzen_stokbroden - aantal_korting

#resultaat
print(" ")
print(f"De feestlunch kost je bij de bakker {round(totaal_met_korting, 2 )} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbroden} stokbroden als de {kortings_bonnen} kortingsbonnen nog geldig zijn!")