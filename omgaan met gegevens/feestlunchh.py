
#prijs per stuk
PRIJS_CROISSANT = 0.39
PRIJS_STOKBROOD = 2.78

#aantallen
aantal_croissant = 17
aantal_stokbroden = 2

KORTINGS_BONNEN = 3
WAARDE_BONNEN = 0.50 

#berekening

prijzen_croissant = aantal_croissant * PRIJS_CROISSANT
prijzen_stokbroden = aantal_stokbroden * PRIJS_STOKBROOD

totaal_kosten_zonder_korting = prijzen_croissant + prijzen_stokbroden
aantal_korting = KORTINGS_BONNEN * WAARDE_BONNEN

totaal_met_korting = prijzen_croissant + prijzen_stokbroden - aantal_korting

#resultaat
print(" ")
print(f"De feestlunch kost je bij de bakker {round(totaal_met_korting, 2 )} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbroden} stokbroden als de {KORTINGS_BONNEN} kortingsbonnen nog geldig zijn!")