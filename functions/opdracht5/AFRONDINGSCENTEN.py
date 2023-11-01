from test_lib import test, report

AFRONDINGSCENTEN = 5

def rond_bedrag_af(origineel_bedrag):
    afgeronde_centen = round(origineel_bedrag * 100)  # Vermenigvuldig met 100 om centen te krijgen
    afgeronde_centen = (afgeronde_centen + AFRONDINGSCENTEN // 2) // AFRONDINGSCENTEN * AFRONDINGSCENTEN  # Rond af op centen van 0 of 5
    afgerond_bedrag = afgeronde_centen / 100  # Terug naar bedrag met twee decimalen
    return afgerond_bedrag


# Vraag de gebruiker om een bedrag in te voeren
origineel_bedrag = float(input("Voer het originele bedrag in: "))
afgeronde_bedrag = rond_bedrag_af(origineel_bedrag)

print(f"Origineel bedrag: {origineel_bedrag}")
print(f"Afgerond bedrag: {afgeronde_bedrag}")
