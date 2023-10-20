gastheer = input("Wie is de gastheer? (Vul de naam in): ")
gasten = int(input("Hoeveel gasten zijn aanwezig? "))
drank = True  # Je kunt de waarde van drank naar True of False aanpassen, afhankelijk van de aanwezigheid van drank
chips = False  # Je kunt de waarde van chips naar True of False aanpassen, afhankelijk van de aanwezigheid van chips

if ((gastheer == "Bjorn" or gastheer == "Slemmers") and gasten >= 0 and gasten <= 20 and (gasten >= 4 or (gasten == 0 and (chips and drank)))):
    print('Start the Party')
else:
    print('No Party')
