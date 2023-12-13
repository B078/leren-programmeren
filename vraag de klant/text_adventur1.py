import time

def intro():
    print("Welkom bij het avontuur! Je bevindt je in een mysterieuze wereld. Probeer te overleven en ontdek de winnende route.")

def actie1():
    print("Actie 1: Je staat voor een kruispunt. Kies tussen 'Links' en 'Rechts'.")
    keuze = input().lower()
    if keuze == "links":
        print("Je gaat naar links en komt bij een verlaten huis.")
        actie2()
    elif keuze == "rechts":
        print("Je gaat naar rechts en belandt in een donker bos.")
        actie3()
    else:
        ongeldige_keuze()

def actie2():
    print("Actie 2: In het verlaten huis vind je een sleutel en een trap naar beneden. Kies tussen 'Trap af' en 'Terug naar het kruispunt'.")
    keuze = input().lower()
    if keuze == "trap af":
        print("Je gaat de trap af en komt in een geheime kamer.")
        actie4()
    elif keuze == "terug naar het kruispunt":
        print("Je keert terug naar het kruispunt.")
        actie1()
    else:
        ongeldige_keuze()

def actie3():
    print("Actie 3: In het donkere bos hoor je geluiden. Kies tussen 'Onderzoeken' en 'Snel verder lopen'.")
    keuze = input().lower()
    if keuze == "onderzoeken":
        print("Je ontdekt een vriendelijke gids die je de weg wijst.")
        actie5()
    elif keuze == "snel verder lopen":
        print("Je loopt snel verder maar struikelt over een boomwortel.")
        verlies("Je hebt jezelf bezeerd en kunt niet verder gaan.")
    else:
        ongeldige_keuze()

def actie4():
    print("Actie 4: In de geheime kamer zie je drie deuren. Kies tussen 'Deur 1', 'Deur 2' en 'Deur 3'.")
    keuze = input().lower()
    if keuze == "deur 1":
        print("Achter de deur vind je een schat.")
        win("Gefeliciteerd! Je hebt de schat gevonden.")
    elif keuze == "deur 2" or keuze == "deur 3":
        print("Achter de deur is een val en je wordt gevangen.")
        verlies("Je bent in een val gelopen en kunt niet ontsnappen.")
    else:
        ongeldige_keuze()

def actie5():
    print("Actie 5: De gids biedt je een magische amulet aan. Kies tussen 'Accepteren' en 'Weigeren'.")
    keuze = input().lower()
    if keuze == "accepteren":
        print("Het amulet beschermt je tegen gevaren.")
        actie6()
    elif keuze == "weigeren":
        print("Je weigert het amulet en gaat alleen verder.")
        actie7()
    else:
        ongeldige_keuze()

def actie6():
    print("Actie 6: Je komt bij een rivier zonder brug. Kies tussen 'Zwemmen' en 'Langs de rivier lopen'.")
    keuze = input().lower()
    if keuze == "zwemmen":
        print("Het amulet beschermt je tegen de sterke stroming en je zwemt veilig naar de overkant.")
        actie8()
    elif keuze == "langs de rivier lopen":
        print("Je volgt de rivier en komt bij een brug.")
        actie4()
    else:
        ongeldige_keuze()

def actie7():
    print("Actie 7: Je komt bij een oude tempel. Kies tussen 'Binnen gaan' en 'Verder lopen'.")
    keuze = input().lower()
    if keuze == "binnen gaan":
        print("Je ontdekt een geheime doorgang onder de tempel.")
        actie8()
    elif keuze == "verder lopen":
        print("Je loopt verder en komt bij een gevaarlijk moeras.")
        verlies("Je zakt weg in het moeras en komt vast te zitten.")
    else:
        ongeldige_keuze()

def actie8():
    print("Actie 8: Je staat voor een magische spiegel. Kies tussen 'Kijken in de spiegel' en 'Langs de spiegel lopen'.")
    keuze = input().lower()
    if keuze == "kijken in de spiegel":
        print("Je ziet de toekomst en krijgt waardevolle aanwijzingen.")
        actie9()
    elif keuze == "langs de spiegel lopen":
        print("Je negeert de spiegel en gaat verder.")
        actie10()
    else:
        ongeldige_keuze()

def actie9():
    print("Actie 9: Je komt bij een betoverd bos. Kies tussen 'Het bos betreden' en 'Een andere route zoeken'.")
    keuze = input().lower()
    if keuze == "het bos betreden":
        print("Je wordt omringd door betoverende wezens maar ze doen je geen kwaad.")
        actie10()
    elif keuze == "een andere route zoeken":
        print("Je zoekt een andere route en vermijdt het betoverde bos.")
        actie10()
    else:
        ongeldige_keuze()

def actie10():
    print("Actie 10: Je bereikt een verlaten kasteel. Kies tussen 'Naar binnen gaan' en 'Rond het kasteel lopen'.")
    keuze = input().lower()
    if keuze == "naar binnen gaan":
        print("Binnen vind je een portaal naar huis. Je hebt het avontuur overleefd!")
        win("Gefeliciteerd! Je hebt de weg naar huis gevonden.")
    elif keuze == "rond het kasteel lopen":
        print("Terwijl je rondloopt, stort een deel van het kasteel in en verspert de weg naar binnen.")
        verlies("Je kunt niet meer naar binnen en bent gestrand.")
    else:
        ongeldige_keuze()

def win(boodschap):
    print(boodschap)
    print("Geweldig! Je hebt gewonnen.")
    exit()

def verlies(boodschap):
    print(boodschap)
    print("Helaas, je hebt verloren.")
    exit()

def ongeldige_keuze():
    print("Ongeldige keuze. Probeer opnieuw.")
    exit()

def main():
    intro()
    actie1()

if __name__ == "__main__":
    main()
