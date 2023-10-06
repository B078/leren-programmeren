#Variabelen
aantal_spelers = 4
prijs_per_periode_persoon = 0.37
totaal_aantal_minuten = 45
toegansticket = 7.45
VR_PERIODE =  5

#Berekeningnen
totaal_per_persoon = ((prijs_per_periode_persoon / VR_PERIODE ) * totaal_aantal_minuten) + toegansticket
totale_kosten = totaal_per_persoon * aantal_spelers

#Print resultaat
print("Totaal is Є" ,round(totale_kosten, 2 ))
print(f"Dit geweldige dagje-uit met {aantal_spelers} mensen in de Speelhal met {totaal_aantal_minuten} minuten VR kost je maar 44.44 euro")

