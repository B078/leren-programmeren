gastheer = input("Wie is de gastheer? (Vul de naam in): ")
gasten = int(input("Hoeveel gasten zijn aanwezig? "))
drank = True  # Je kunt de waarde van drank naar True of False aanpassen, afhankelijk van de aanwezigheid van drank
chips = True  # Je kunt de waarde van chips naar True of False aanpassen, afhankelijk van de aanwezigheid van chips


party_gasten = gasten >=4 and gasten <=20 and chips and drank and gastheer != "Slemmer"
party_gastheer = gastheer > "" and drank and gastheer != "Slemmer"
party_me = gastheer == "Bjorn" 

if party_gasten or party_gastheer or party_me:
    print('Start the Party')
else:
    print('No Party')
