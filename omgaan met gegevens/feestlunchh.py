
#prijs per stuk
prijs_croissant = 0.39
prijs_stokbrood = 2.78

#aantallen
aantal_croissant = 17
aantal_stokbroden = 2

#berekening

prijzen_croissant = aantal_croissant * prijs_croissant
prijzen_stokbroden = aantal_stokbroden * prijs_stokbrood

totaal = prijzen_croissant + prijzen_stokbroden

#resultaat
print("Het te betalen bedrag is $",round(totaal, 2 ))
      