#waardes 
arbeid_kosten_per_band = 15.00
arbeid_lampje_vervangen_per_lamp = 2.10

nieuwe_band = 75.79
nieuwe_lampje = 1.45

import time 

print("Welkom bij Scooterzaak Verschoor.")
time.sleep(1)
print(" ")
print("Waar mee kan ik u helpen? ")
opdracht = input("reparatie/showroom? ")
print(" ")


if opdracht == "reparatie":
    time.sleep(0.3)
    print("|---------------|")
    print("| • 1. banden   |")
    print("| • 2. lampen   |")
    print("| • 3. beide    |")
    print("|---------------|")
    time.sleep(0.5)
    vraag = input("Voer het getal in dat u nodig heeft: ")

    if "1" in vraag:
        time.sleep(0.3)
        print(" ")
        print("<--------------------------->")
        aantal_banden = int(input("Hoeveel banden heeft u nodig? "))
        print(" ")
        time.sleep(0.5)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")

        kosten_banden = nieuwe_band * aantal_banden
        arbeid_banden = arbeid_kosten_per_band * aantal_banden
        totaal_banden = kosten_banden + arbeid_banden


        print(" ")
        print("<---------BON-------->")
        print(f"Nieuwe banden: {aantal_banden}   prijs: {kosten_banden}")
        print(f"Arbeid per band: {aantal_banden} prijs: {round(arbeid_kosten_per_band, 2 )}")
        print(f"Uw te betalen bedrag is ${totaal_banden}")

    elif "2" in vraag:
        time.sleep(0.3)
        print(" ")
        print("<--------------------------->")
        int(input("Hoeveel lampen heeft u nodig? "))
        print(" ")
        time.sleep(0.5)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")

       
    
    elif "3" in vraag:
        time.sleep(0.3)
        print(" ")
        print("<--------------------------->")
        aantal_banden = int(input("Hoeveel banden heeft u nodig? "))
        print(" ")
        time.sleep(0.3)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(3)

        print(" ")
        print("<-------------------------->")
        aantal_lampjes = int(input("Hoeveel lampen heeft u nodig? "))
        print(" ")
        time.sleep(0.3)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(3)
        #berekening
        
        kosten_banden = nieuwe_band * aantal_banden
        kosten_lampen = nieuwe_lampje * aantal_lampjes
        totaal_banden = kosten_banden+ (arbeid_kosten_per_band * aantal_banden)
        totaal_lampen = kosten_lampen + (arbeid_lampje_vervangen_per_lamp * aantal_lampjes)
        totaal1 = totaal_banden + totaal_lampen

        print("<----------BON-------->")
        print(f"Nieuwe banden: {aantal_banden} prijs: {kosten_banden}")
        print(f"Nieuwe lampen: {aantal_lampjes} prijs: {nieuwe_lampje}")
        print(f"Arbeid per band: {arbeid_kosten_per_band}")
        print(f"Arbeid per lamp: {arbeid_lampje_vervangen_per_lamp}")
        print(f"Totale kosten is $,{round(totaal1, 2 )}")
        

    else:
        print("fout")  