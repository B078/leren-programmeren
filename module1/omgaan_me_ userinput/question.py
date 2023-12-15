#gegevens 
while True:
    naam = input("hallo, wat is je naam? ")
    leeftijd = input(f"goedendag {naam}, hoe oud ben je? ")
    lievelings_eten = input(f"en als {leeftijd} jarige, wat eet je het liefst? ")
    lievelings_drinken = input(f"en wat drink je het liefst bij {lievelings_eten}? ")
#output
    print(" ")
    print(f"de {leeftijd} jarige {naam} drinkt het liefst een {lievelings_drinken} bij {lievelings_eten}")

    print()
    antwoord = input("Wil je nog een keer proberen? (ja/nee) ")
    if antwoord.lower() != "ja":
      break