#constanten
TOEGANGTICKET = 745
PRIJS_PER_PERIODE_PERSOON = 37
VR_PERIODE =  5

aantal_spelers = int(input("met hoeveel personen bent u? "))
print(" ")
print("--------disclaimer-------")
print("kosten vr per 5 min 0.37 pp")
print("--------disclaimer-------")
print(" ")
totaal_aantal_minuten = int(input("hoeveel minuten willen jullie in de vr? "))
#Berekeningnen
totaal_per_persoon = (((PRIJS_PER_PERIODE_PERSOON / VR_PERIODE ) * totaal_aantal_minuten) + TOEGANGTICKET ) /100
totale_kosten = totaal_per_persoon * aantal_spelers

#Print resultaat
print("Totaal is Є" ,round(totale_kosten, 2 ))
print(f"Dit geweldige dagje-uit met {aantal_spelers} mensen in de Speelhal met {totaal_aantal_minuten} minuten VR kost je maar {totale_kosten} euro")

