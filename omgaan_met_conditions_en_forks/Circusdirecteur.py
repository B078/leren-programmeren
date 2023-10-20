#vacature Circusdirecteur voor Circus HotelDeBotel
import time

print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
print("        sollicatieformulier 'Circusdirecteur' ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
print("U begint nu aan uw sollicitatie voor Circusdirecteur voor Circus HotelDeBotel")
print("hierbij komen een aantal vragen")
print("probeert u deze zo eerlijk mogelijk te beantwoorden")
print("- - - - - - - - - -  - -  - - - - - - - - - - - - ")

#gegevens opvagen
time.sleep(2)
naam = input("Wat is uw naam? ")
rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? (J/N) ")
hoge_houd = input("Bent u in bezit van een hoge hoed? (J/N) ")
lichaamsgewicht = float(input("Wat is uw lichaamsgewicht? (kg) "))
lichaamslengte = int(input("Wat is uw lichaamslengte? (hele cm) "))
certificaat = input("Heeft u een Certificaat overleven met gevaarlijk personeel? (J/N) ")
print("- - - - - - - ervarings vragen - - - - - - - -")
time.sleep(1)
ervaring_dieren_dressuur = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar heeft u ervaring met jongleren? "))
ervaring_acrobatiek = int(input("Hoeveel jaar heeft u praktijkervaring met acrobatiek? "))

#berekening
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_ERVARING_DIER = 4
MIN_ERVARING_JONGLEREN = 5
MIN_ERVARING_ACROBATIEK = 3

passed = True

if rijbewijs.lower() != "j":
    passed = False

if hoge_houd.lower() != "j":
    passed = False

if not (MIN_WEIGHT <= lichaamsgewicht <= MAX_WEIGHT):
    passed = False

if not (MIN_LENGTE <= lichaamslengte <= MAX_LENGTE):
    passed = False

if certificaat.lower() != "j":
    passed = False

if ervaring_dieren_dressuur < MIN_ERVARING_DIER:
    passed = False

if ervaring_jongleren < MIN_ERVARING_JONGLEREN:
    passed = False

if ervaring_acrobatiek < MIN_ERVARING_ACROBATIEK:
    passed = False

if passed:
    print(f"Gefeliciteerd! {naam}. U komt in aanmerking voor de functie Circus Directeur..")
else:
    print(f"Helaas {naam}. U voldoet niet aan onze eisen voor Circus Directeur. Het spijt ons.")
