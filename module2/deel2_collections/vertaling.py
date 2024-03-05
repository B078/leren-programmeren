def vertaal_tekst(tekst, vertaal_woordenboek):
    woorden = tekst.split()
    vertaalde_tekst = []

    for woord in woorden:
        vertaalde_tekst.append(vertaal_woordenboek.get(woord, woord))

    return ' '.join(vertaalde_tekst)


# Definieer het vertaalwoordenboek
vertaal_woordenboek = {
    'het hart': 'de ingang',
    'grot': 'grot',
    'Draganthor': 'Draganthor',
    'schubben': 'teennagels',
    'vurige': 'waterende',
    'ogen': 'ogen',
    'draak': 'geit',
    'brulde': 'brulde',
    'spuwde': 'spuwde',
    'vlammenzee': 'golf van water',
    'bedreigde': 'bedreigde',
    'Rurik': 'Rurik',
    'beschermde': 'beschermde',
    'krachtig': 'krachtig',
    'schild': 'zwemvliezen',
    'magie': 'plastic'
}

# Vraag om input van de gebruiker
originele_tekst = input("Voer een stuk tekst in: ")

# Vertaal de tekst
vertaalde_tekst = vertaal_tekst(originele_tekst, vertaal_woordenboek)

# Toon de vertaalde tekst
print("\nVertaalde tekst:")
print(vertaalde_tekst)
