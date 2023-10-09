#waardes 
arbeid_kosten_per_band = 15.00
arbeid_lampje_vervangen_per_lamp = 2.10

nieuwe_band = 75.79
nieuwe_lampje = 1.45

aantal_banden = 2 
aantal_lampjes = 2 

import time 

print("Welkom bij Scooterzaak Verschoor.")
time.sleep(1)
print(" ")
print("Waar mee kan ik u helpen? ")
opdracht = input("reparatie/showroom? ")
print(" ")


if opdracht == "reparatie":
    time.sleep(1)
    print("Wat wilt u gerepareerd heben? ")
    time.sleep(0.3)
    print("|-----------|")
    print("| •banden   |")
    print("| •lampen   |")
    print("| •beide    |")
    print("|-----------|")
    time.sleep(0.5)
    vraag = input(":banden / lampen of beide? ")

    if "beide" in vraag:
        time.sleep(0.3)
        print(" ")
        print("<--------------------------->")
        int(input("Hoeveel banden heeft u nodig? "))
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
        int(input("Hoeveel lampen heeft u nodig? "))
        print(" ")
        time.sleep(0.3)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(3)
        
    
        

    elif "banden" in vraag:
        time.sleep(0.3)
        print(" ")
        print("<--------------------------->")
        int(input("Hoeveel banden heeft u nodig? "))
        print(" ")
        time.sleep(0.5)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
        time.sleep(1)
        print("Moment geduld a.u.b., bestelling opslaan")
       

    elif "lampen" in vraag:
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
        

    else:
        print("fout")