from test_lib import test, report

AFRONDINGSCENTEN = 5

def rond_bedrag_af(origineel_bedrag):
    afgerond_bedrag = round(origineel_bedrag * 20) / 20
    return afgerond_bedrag

# Vraag de gebruiker om een bedrag in te voeren
origineel_bedrag = float(input("Voer het originele bedrag in: "))
afgeronde_bedrag = rond_bedrag_af(origineel_bedrag)

print(f"Origineel bedrag: {origineel_bedrag}")
print(f"Afgerond bedrag: {afgeronde_bedrag}")
