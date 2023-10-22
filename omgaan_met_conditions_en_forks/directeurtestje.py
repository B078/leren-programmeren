import time

print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
print("      sollicitatieformulier 'Circusdirecteur' ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
print("U begint nu aan uw sollicitatie voor Circusdirecteur voor Circus HotelDeBotel")
print("hierbij komen een aantal vragen")
print("probeert u deze zo eerlijk mogelijk te beantwoorden")
print("- - - - - - - - - -  - -  - - - - - - - - - - - - ")

# Gegevens opvragen
# Vereiste vragen 
time.sleep(2)
naam = input("Wat is uw naam? ")
rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? (J/N) ")
hoge_hoed = input("Bent u in bezit van een hoge hoed? (J/N) ")
lichaamsgewicht = float(input("Wat is uw lichaamsgewicht? (kg) "))
lichaamslengte = int(input("Wat is uw lichaamslengte? (hele cm) "))
certificaat = input("Heeft u een Certificaat overleven met gevaarlijk personeel? (J/N) ")
print("- - - - - - - ervaringsvragen - - - - - - - -") # Ervaring gedeelte
time.sleep(1)
ervaring_dieren_dressuur = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar heeft u ervaring met jongleren? "))
ervaring_acrobatiek = int(input("Hoeveel jaar heeft u praktijkervaring met acrobatiek? "))
print("- - - - persoonlijke vragen - - - - - -") # Persoonlijk gedeelte
time.sleep(1)
bezit_diploma = input("Bent u in bezit van een MBO-4 Diploma ondernemen? (J/N) ")
jaren_ondernemer = int(input("Hoeveel jaar bent u al ondernemer? "))
aantal_werknemer_loondienst = int(input("Hoeveel werknemers heeft u in loondienst? "))
geslacht = input("Wat is uw geslacht? (man/vrouw/anders) ")

if geslacht == "man":
    snor_breedte = int(input("Hoeveel cm is uw snor breed? (hele cm) "))

elif  geslacht == "vrouw":
    soort_haar = input("Wat voor soort haar heeft u? ")
    if soort_haar == "rood krulhaar":
        lengte_haar = int(input("Hoeveel cm is uw haar? (hele cm) "))

elif geslacht == "anders":
    breedte_glimlach = int(input("Hoeveel cm is uw glimlach in breedte (hele cm) "))

redenen_mannen = []
redenen_vrouwen = []
redenen_anderen = []

# constanten
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_ERVARING_DIER = 4
MIN_ERVARING_JONGLEREN = 5
MIN_ERVARING_ACROBATIEK = 3
MIN_ONDERNEMER = 3
MIN_LOONDIENST_WERKNEMERS = 5
MAN_SNOR = 10
VROUW_LENGTE_HAAR = 20
BREEDTE_GLIMLACH = 10

#berekening 
if geslacht == "man":
    if rijbewijs.lower() != "j":
        redenen_mannen.append("U heeft geen vrachtwagen rijbewijs.")
    if hoge_hoed.lower() != "j":
        redenen_mannen.append("U bezit geen hoge hoed.")
    if not (MIN_WEIGHT <= lichaamsgewicht <= MAX_WEIGHT):
        redenen_mannen.append("Uw lichaamsgewicht voldoet niet aan de vereisten.")
    if not (MIN_LENGTE <= lichaamslengte <= MAX_LENGTE):
        redenen_mannen.append("Uw lichaamslengte voldoet niet aan de vereisten.")
    if certificaat.lower() != "j":
        redenen_mannen.append("U heeft geen Certificaat overleven met gevaarlijk personeel.")
    if ervaring_dieren_dressuur < MIN_ERVARING_DIER and ervaring_jongleren < MIN_ERVARING_JONGLEREN and ervaring_acrobatiek < MIN_ERVARING_ACROBATIEK:
        redenen_mannen.append("U heeft onvoldoende ervaring in dieren-dressuur, jongleren en acrobatiek.")
    if bezit_diploma.lower() != "j" and jaren_ondernemer < MIN_ONDERNEMER or aantal_werknemer_loondienst < MIN_LOONDIENST_WERKNEMERS:
        redenen_mannen.append("U voldoet niet aan de ondernemersvereisten.")
    if snor_breedte < MAN_SNOR:
        redenen_mannen.append("Uw snor is niet breed genoeg.")

elif geslacht == "vrouw":
    if rijbewijs.lower() != "j":
        redenen_vrouwen.append("U heeft geen vrachtwagen rijbewijs.")
    if hoge_hoed.lower() != "j":
        redenen_vrouwen.append("U bezit geen hoge hoed.")
    if not (MIN_WEIGHT <= lichaamsgewicht <= MAX_WEIGHT):
        redenen_vrouwen.append("Uw lichaamsgewicht voldoet niet aan de vereisten.")
    if not (MIN_LENGTE <= lichaamslengte <= MAX_LENGTE):
        redenen_vrouwen.append("Uw lichaamslengte voldoet niet aan de vereisten.")
    if certificaat.lower() != "j":
        redenen_vrouwen.append("U heeft geen Certificaat overleven met gevaarlijk personeel.")
    if ervaring_dieren_dressuur < MIN_ERVARING_DIER and ervaring_jongleren < MIN_ERVARING_JONGLEREN and ervaring_acrobatiek < MIN_ERVARING_ACROBATIEK:
        redenen_vrouwen.append("U heeft onvoldoende ervaring in dieren-dressuur, jongleren en acrobatiek.")
    if bezit_diploma.lower() != "j" and jaren_ondernemer < MIN_ONDERNEMER or aantal_werknemer_loondienst < MIN_LOONDIENST_WERKNEMERS:
        redenen_vrouwen.append("U voldoet niet aan de ondernemersvereisten.")
    if soort_haar == "rood krulhaar" and lengte_haar < VROUW_LENGTE_HAAR:
        redenen_vrouwen.append("Uw haar is niet lang genoeg.")

elif geslacht == "anders":
    if rijbewijs.lower() != "j":
        redenen_anderen.append("U heeft geen vrachtwagen rijbewijs.")
    if hoge_hoed.lower() != "j":
        redenen_anderen.append("U bezit geen hoge hoed.")
    if not (MIN_WEIGHT <= lichaamsgewicht <= MAX_WEIGHT):
        redenen_anderen.append("Uw lichaamsgewicht voldoet niet aan de vereisten.")
    if not (MIN_LENGTE <= lichaamslengte <= MAX_LENGTE):
        redenen_anderen.append("Uw lichaamslengte voldoet niet aan de vereisten.")
    if certificaat.lower() != "j":
        redenen_anderen.append("U heeft geen Certificaat overleven met gevaarlijk personeel.")
    if ervaring_dieren_dressuur < MIN_ERVARING_DIER and ervaring_jongleren < MIN_ERVARING_JONGLEREN and ervaring_acrobatiek < MIN_ERVARING_ACROBATIEK:
        redenen_anderen.append("U heeft onvoldoende ervaring in dieren-dressuur, jongleren en acrobatiek.")
    if bezit_diploma.lower() != "j" and jaren_ondernemer < MIN_ONDERNEMER or aantal_werknemer_loondienst < MIN_LOONDIENST_WERKNEMERS:
        redenen_anderen.append("U voldoet niet aan de ondernemersvereisten.")
    if breedte_glimlach < BREEDTE_GLIMLACH:
        redenen_anderen.append("U glimlach is niet lang genoeg.")

# Weergave van redenen per geslacht
if geslacht == "man":
    if not redenen_mannen:
        print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")
    else:
        print(f"Sorry, {naam}, u komt niet in aanmerking voor de functie om de volgende redenen:")
        for reden in redenen_mannen:
            print(f"- {reden}")

elif geslacht == "vrouw":
    if not redenen_vrouwen:
        print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")
    else:
        print(f"Sorry, {naam}, u komt niet in aanmerking voor de functie om de volgende redenen:")
        for reden in redenen_vrouwen:
            print(f"- {reden}")
elif geslacht == "anders":

    if not redenen_anderen:
        print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")
    else:
        print(f"Sorry, {naam}, u komt niet in aanmerking voor de functie om de volgende redenen:")
        for reden in redenen_anderen:
            print(f"- {reden}")
