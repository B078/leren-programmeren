# Vraag de gebruiker om persoonlijke informatie
naam = input("Wat is uw naam? ")
adres = input("Wat is uw adres? ")
postcode = input("Wat is uw postcode? ")
woonplaats = input("Wat is uw woonplaats? ")

# Toon de aangepaste adreskaart
print("-" * 40)
print(f"|  Naam      : {naam:<23}  |")
print(f"|  Adres     : {adres:<23}  |")
print(f"|  Postcode  : {postcode:<23}  |")
print(f"|  Woonplaats: {woonplaats:<23}  |")
print("-" * 40)