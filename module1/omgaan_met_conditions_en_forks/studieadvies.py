from studadviestext import *
import time


AANTAL_VRAGEN_10w = 7
AANTAL_VRAGEN = 5
ALTIJD = 0
VAAK = 1
REGELMATIG = 2
SOMS = 3
NOOIT = 4

print(STUDIEDOKTER_TITEL)
time.sleep(2)
print(AANTAL_WEKEN_VRAAG)
aantal_weken = int(input(""))


#berekenen
print(COMPETENTIE_STELLING_1)
print(OPTIES)
ans_vraag1 = int(input(""))
print(COMPETENTIE_STELLING_2)
print(OPTIES)
ans_vraag2 = int(input(""))
print(COMPETENTIE_STELLING_3)
print(OPTIES)
ans_vraag3 = int(input(""))
print(COMPETENTIE_STELLING_4)
print(OPTIES)
ans_vraag4 = int(input(""))
print(COMPETENTIE_STELLING_5)
print(OPTIES)
ans_vraag5 = int(input(""))
if aantal_weken >= 10:
    print(COMPETENTIE_STELLING_6)
    print(OPTIES)
    ans_vraag6 = int(input(""))
    print(COMPETENTIE_STELLING_7)
    print(OPTIES)
    ans_vraag7 = int(input(""))

    aantal_punten_per_vraag = [ans_vraag1, ans_vraag2, ans_vraag3, ans_vraag4, ans_vraag5, ans_vraag6, ans_vraag7]
    aantal_vragen = AANTAL_VRAGEN_10w
else:
    aantal_punten_per_vraag = [ans_vraag1, ans_vraag2, ans_vraag3, ans_vraag4, ans_vraag5]
    aantal_vragen = AANTAL_VRAGEN

# Bereken de totale punten en gemiddelde score
totaal_punten = sum(aantal_punten_per_vraag)
gemiddelde_score = totaal_punten / aantal_vragen

# Definieer de grens voor falen (meer dan de helft van de vragen met score 0 of 1)
grens_falen = aantal_vragen/ 2

# Tel hoeveel vragen zijn beantwoord met score 0 of 1
aantal_faal_scores = sum(score <= 1 for score in aantal_punten_per_vraag)

    # Controleer of de persoon heeft gefaald
if gemiddelde_score <= 2 or aantal_faal_scores > grens_falen:
    print(COMPETENTIE_ADVIES_ZORGELIJK)

# Controleren of de gemiddelde score gelijk is aan 3 of lager
elif gemiddelde_score <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    # Tel hoeveel vragen zijn beantwoord met 'altijd', 'vaak' of 'regelmatig'
    aantal_hoog_scores = sum(score <= REGELMATIG for score in aantal_punten_per_vraag)

    # Definieer de grens voor falen (meer dan de helft van de vragen met 'altijd', 'vaak' of 'regelmatig')
    grens_falen_hoog_scores = AANTAL_VRAGEN / 2

    # Controleren of meer dan de helft van de vragen met 'altijd', 'vaak' of 'regelmatig' is beantwoord
    if aantal_hoog_scores > grens_falen_hoog_scores:
        print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
    else:
        print(COMPETENTIE_ADVIES_GERUSTSTELLEND)

            
