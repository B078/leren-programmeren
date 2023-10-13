import time
#gegevens vragen

print("!vandaag gaan we raad de kaas spelen!")
time.sleep(0.5)
print()

gele_kaas = input("is je kaas geel? (ja/nee) ")
if gele_kaas == "ja":
    gaten_kaas = input("heeft je kaas gaten? (ja/nee) ")
    if gaten_kaas == "ja":
        duur_kaas = input("is uw kaas belachelijk duur? (ja/nee)")
        if duur_kaas == "ja":
            print()
            print("U denkt aan emmenthaler")
        elif duur_kaas == "nee":
            print()
            print(" u denkt aan leerdammer")
    elif gaten_kaas == "nee":
        hard_kaas = input("is uw kaas zo hard als staan? (ja/nee) ")
        if hard_kaas == "ja":
            print("U denkt aan parmigiano reggiano")
        elif hard_kaas == "nee":
            print()
            print("u denkt aan goudse kaas ")
elif gele_kaas == "nee":
    blauwe_kaas = input("heeft de kaas blauwe schimmel? (ja/nee) ")
    if blauwe_kaas == "ja":
        korst_kaas = input("heeft u kaas een korst? (ja/nee) ")
        if korst_kaas == "ja":
            print("u denkt aan Blue de Rochbaron")
        elif korst_kaas == "nee":
            print()
            print("u denkt aan foume d'ambert")
    elif blauwe_kaas == "nee":
        korst_kaas = input("heeft u kaas een korst? (ja/nee) ")
        if korst_kaas == "ja":
            print()
            print("u denkt aan Camembert")
        elif korst_kaas == "nee":
            print()
            print("u denkt aan mozzerella")

time.sleep(1)
print()
print("dank voor het spelen")
        
        
        
  