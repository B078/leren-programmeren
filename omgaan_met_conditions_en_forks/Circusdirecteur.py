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
#vereiste vragen 
time.sleep(2)
naam = input("Wat is uw naam? ")
rijbewijs = input("Bent u in bezit van een vrachtwagen rijbewijs? (J/N) ")
hoge_hoed = input("Bent u in bezit van een hoge hoed? (J/N) ")
lichaamsgewicht = float(input("Wat is uw lichaamsgewicht? (kg) "))
lichaamslengte = int(input("Wat is uw lichaamslengte? (hele cm) "))
certificaat = input("Heeft u een Certificaat overleven met gevaarlijk personeel? (J/N) ")
print("- - - - - - - ervarings vragen - - - - - - - -") #ervaring gedeelte
time.sleep(1)
ervaring_dieren_dressuur = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur? "))
ervaring_jongleren = int(input("Hoeveel jaar heeft u ervaring met jongleren? "))
ervaring_acrobatiek = int(input("Hoeveel jaar heeft u praktijkervaring met acrobatiek? "))
print("- - - - persoonlijke vragen - - - - - -") #persoonlijk gedeelte
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

#berekening
MIN_WEIGHT = 90
MAX_WEIGHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_ERVARING_DIER = 4
MIN_ERVARING_JONGLEREN = 5
MIN_ERVARING_ACROBATIEK = 3
MIN_ONDERMER = 3
MIN_LOONDIENST_WERKNEMERS = 5
MAN_SNOR = 10
VROUW_LENGTE_HAAR = 20

if geslacht == "man":
    if rijbewijs.lower() == "j":
        if hoge_hoed.lower() == "j":
            if lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT:
                if lichaamslengte >= MIN_LENGTE and lichaamslengte <= MAX_LENGTE:
                    if certificaat.lower() == "j":
                        if ervaring_dieren_dressuur >= 4 or ervaring_jongleren >= 5 or ervaring_acrobatiek >= 3:
                            if bezit_diploma.lower() == "j" or jaren_ondernemer >= 3 and aantal_werknemer_loondienst >= 5:
                                if snor_breedte >= 10:
                                    print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")    
                                else:
                                    print("helaas u voldoet niet aan de vereisten.") 
                            else:
                                print("helaas u voldoet niet aan de vereisten.") 
                        else:
                            print("helaas u voldoet niet aan de vereisten.") 
                    else:
                        print("helaas u voldoet niet aan de vereisten.") 
                else:
                    print("helaas u voldoet niet aan de vereisten.") 
            else:
                print("helaas u voldoet niet aan de vereisten.") 
        else:
            print("helaas u voldoet niet aan de vereisten.") 
    else:
        print("helaas u voldoet niet aan de vereisten.") 
else:
    print("helaas u voldoet niet aan de vereisten.")                              


if geslacht == "vrouw":
    if rijbewijs.lower() == "j":
        if hoge_hoed.lower() == "j":
            if lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT:
                if lichaamslengte >= MIN_LENGTE and lichaamslengte <= MAX_LENGTE:
                    if certificaat.lower() == "j":
                        if ervaring_dieren_dressuur >= 4 or ervaring_jongleren >= 5 or ervaring_acrobatiek >= 3:
                            if bezit_diploma.lower() == "j" or jaren_ondernemer >= 3 and aantal_werknemer_loondienst >= 5:
                                if soort_haar == "rood krulhaar":
                                    if lengte_haar >= 20:
                                        print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")
                                    else:
                                        print("helaas u voldoet niet aan de vereisten.") 
                                else:
                                    print("helaas u voldoet niet aan de vereisten.") 
                            else:
                                print("helaas u voldoet niet aan de vereisten.") 
                        else:
                            print("helaas u voldoet niet aan de vereisten.") 
                    else:
                        print("helaas u voldoet niet aan de vereisten.") 
                else:
                    print("helaas u voldoet niet aan de vereisten.") 
            else:
                print("helaas u voldoet niet aan de vereisten.") 
        else:
            print("helaas u voldoet niet aan de vereisten.") 
    else:
        print("helaas u voldoet niet aan de vereisten.") 
else:
    print("helaas u voldoet niet aan de vereisten.")


if geslacht == "anders":
    if rijbewijs.lower() == "j":
        if hoge_hoed.lower() == "j":
            if lichaamsgewicht >= MIN_WEIGHT and lichaamsgewicht <= MAX_WEIGHT:
                if lichaamslengte >= MIN_LENGTE and lichaamslengte <= MAX_LENGTE:
                    if certificaat.lower() == "j":
                        if ervaring_dieren_dressuur >= 4 or ervaring_jongleren >= 5 or ervaring_acrobatiek >= 3:
                            if bezit_diploma.lower() == "j" or jaren_ondernemer >= 3 and aantal_werknemer_loondienst >= 5:
                                if breedte_glimlach >= 10:
                                    print(f"Gefeliciteerd {naam}, u komt in aanmerking voor de functie.")
                                else:
                                    print("helaas u voldoet niet aan de vereisten.") 
                            else:
                                print("helaas u voldoet niet aan de vereisten.") 
                        else:
                            print("helaas u voldoet niet aan de vereisten.") 
                    else:
                        print("helaas u voldoet niet aan de vereisten.") 
                else:
                    print("helaas u voldoet niet aan de vereisten.") 
            else:
                print("helaas u voldoet niet aan de vereisten.") 
        else:
            print("helaas u voldoet niet aan de vereisten.") 
    else:
        print("helaas u voldoet niet aan de vereisten.") 
else:
    print("helaas u voldoet niet aan de vereisten.") 