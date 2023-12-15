def start_game():
    print("Welkom bij het text adventure!")
    print("Je bevindt je voor een oude, mysterieuze grot. Er zijn twee paden voor je: links en rechts.")

    while True:
        keuze1 = input("Welk pad kies je? (links/rechts): ").lower()

        if keuze1 == "links":
            pad_links()
            break
        elif keuze1 == "rechts":
            pad_rechts()
            break
        else:
            print("Ongeldige keuze. Kies opnieuw.")

def pad_links():
    print("Je betreedt een donkere tunnel. Plotseling hoor je gerommel achter je.")
    print("Wat doe je?")
    
    keuze2 = input("1. Snel verder lopen\n2. Terugkeren en het andere pad nemen\n")

    if keuze2 == "1":
        print("Je rent verder, maar struikelt over een steen en valt in een diepe kuil. Game Over!")
    elif keuze2 == "2":
        print("Je keert terug naar de splitsing.")
        start_game()
    else:
        print("Ongeldige keuze. Game Over!")

def pad_rechts():
    print("Je komt in een grote open ruimte met drie deuren: rood, blauw en groen.")
    print("Welke deur kies je?")

    keuze3 = input("1. Rode deur\n2. Blauwe deur\n3. Groene deur\n")

    if keuze3 == "1":
        print("Je opent de rode deur en vindt een schatkist! Je hebt gewonnen!")
    elif keuze3 == "2":
        print("Achter de blauwe deur is een woeste draak die je verslindt. Game Over!")
    elif keuze3 == "3":
        print("Je opent de groene deur en belandt in een betoverend bos. Je hebt gewonnen!")
    else:
        print("Ongeldige keuze. Game Over!")

if __name__ == "__main__":
    start_game()
