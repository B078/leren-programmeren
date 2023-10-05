#Variabelen
aantal_spelers = 4
prijs_per_5_minuten = 0.37
totaal_aantal_minuten = 45
toegansticket = 7.45

#Berekeningnen
totaal_per_persoon = ((prijs_per_5_minuten / 5 ) * totaal_aantal_minuten) + toegansticket
totale_kosten = totaal_per_persoon * aantal_spelers

#Print resultaat
print("Є" ,round(totale_kosten, 2 ))