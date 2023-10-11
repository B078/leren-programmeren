
#constanten
PRIJS_CROISSANT = 0.39
PRIJS_STOKBROOD = 2.78

aantal_croissanten = int(input("hoeveel croissanten had u gewild? "))
aantal_stokbroden = int(input("hoeveel stokbroden had u gewild? "))

aantal_kortings_bonnen = int(input("hoeveel kortingsbonnen heeft u? "))
waarde_korting = int(input("wat is de waarde van de bon? "))

#berekening

prijzen_croissant = aantal_croissanten * PRIJS_CROISSANT
prijzen_stokbroden = aantal_stokbroden * PRIJS_STOKBROOD

totaal_kosten_zonder_korting = prijzen_croissant + prijzen_stokbroden 

aantal_korting = aantal_kortings_bonnen * (waarde_korting / 100)
totaal_met_korting = totaal_kosten_zonder_korting - aantal_korting

#resultaat
print(" ")
print(f"Uw korting met de bonnen is ${aantal_korting}")
print(f"De feestlunch kost je bij de bakker {round(totaal_met_korting, 2 )} euro voor de {aantal_croissanten} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortings_bonnen} kortingsbonnen nog geldig zijn!")