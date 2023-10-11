#voornaam bjorn
#achternaa verschoor
#opdraccht pizzacalculator

#constanten waarde
PRIJS_SMALL_PIZZA = 6.99
PRIJS_MEDIUM_PIZZA = 12.49
PRIJS_LARGE_PIZZA = 16.99

#gegevens
print("-------prijzenlijst-----")
print(f"small pizza prijs:  {PRIJS_SMALL_PIZZA}  euro")
print(f"medium pizza prijs: {PRIJS_MEDIUM_PIZZA} euro")
print(f"large pizza prijs:  {PRIJS_LARGE_PIZZA} euro")
print("------prijzenlijst------")

#vraag gebruiker aantal per afmeting
aantal_small_pizza = int(input("Hoeveel small pizza's wilt u hebben? "))
aantal_medium_pizza = int(input("Hoeveel medium pizza's wilt u hebben? "))
aantal_large_pizza = int(input("Hoeveel large pizza's wilt u hebben? "))

#berekening
totaal_small = PRIJS_SMALL_PIZZA * aantal_small_pizza
totaal_medium = PRIJS_MEDIUM_PIZZA * aantal_medium_pizza
totaal_large = PRIJS_LARGE_PIZZA * aantal_large_pizza

totaal_kosten = totaal_small + totaal_medium + totaal_large

#output
print(" ")
print("- - - - - - - - - - - - - - - - - - - - - - ")
print("bestelingoverzicht: ")
print(f"{aantal_small_pizza} small  pizza's: {round(totaal_small, 2)} euro")
print(f"{aantal_medium_pizza} medium pizza's: {round(totaal_medium, 2)} euro")
print(f"{aantal_large_pizza} large  pizza's: {round(totaal_large, 2 )} euro")
print("- - - - - - - - - - - - - - - - - - - - - - ")
print(f"Uw totaal te betalen bedrag is {round(totaal_kosten, 2)} euro")
