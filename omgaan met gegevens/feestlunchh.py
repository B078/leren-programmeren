
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

print(f"Uw te betalen bedrag is, {round(totaal, 2)} ")