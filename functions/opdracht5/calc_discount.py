from test_lib import test, report
#variable en constan
month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

#funtion
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:

    discount_brands = month_discount_brands.split(",") #split komma bij de merken 
#kijken voor de merk in de lijst
    if brand in discount_brands:
        discount = (price * MONTH_DISCOUNT_PERC) / 100
        return round(discount, 2)
    else:
        return 0.0

brand = input("Voer het merk in ")
price = float(input("Wat is de prijs? "))

# Bereken en toon de korting
discounts = calc_discount(price, brand, month_discount_brands)
totaal_bedrag = price - discounts
afgerond_totaal = round(totaal_bedrag, 2)

print()
print(f"Uw gekozen merk is: {brand}")
print(f"Uw korting voor het merk is: {discounts} euro")
print(f"U totaal bedrag om te betalen is: {afgerond_totaal} euro")