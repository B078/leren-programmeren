import time
# ANSI escape codes for text colors
class TextColors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    #TextColors.BLACK + "" + TextColors.RESET

print(TextColors.RED + "\n       Welkom bij mijn spel        " + TextColors.RESET)
print(TextColors.WHITE + "U bent in dienst van de 11e Luchtmobiele Brigrade Alfa compangie." + TextColors.RESET)
print(TextColors.WHITE + "U missie is om de vijandelijke opperbevelhebber neutraliseren." + TextColors.RESET)
print(TextColors.WHITE + "Je krijgt meerdere problemen die je met je team moet oplossen, zorg dat je het overleefd en de missie haalt." + TextColors.RESET)
time.sleep(2)
print(TextColors.WHITE + "Location:" + TextColors.RED + " Moscow" + TextColors.RED  + TextColors.RESET)
print(TextColors.WHITE + "        Mission:" + TextColors.RED + " Tango down" + TextColors.RED + TextColors.RESET)
print(TextColors.WHITE + "Date:" + TextColors.RED + " 06-08-18\n" + TextColors.RED  + TextColors.RESET)
time.sleep(3)
print(TextColors.WHITE + "Je bent met je peleton geland in het stadje: Ljoebertsy op zo 20km van het doelwit." + TextColors.RESET) 
time.sleep(2)
print(TextColors.WHITE + "Je bent commadant en maakt dus de keuzes. Die moet je nu hier ook maken." + TextColors.RESET)
time.sleep(2)
print(TextColors.WHITE + "Hoe wil je in Moscow aan komen?" + TextColors.RESET)
input_vraag1 = TextColors.BLUE + "Ga je lopen met je groep of jat je een auto zodat je sneller bij je doelwit bent?" + TextColors.RESET + " (lopen / jatten): " 
vraag1 = input(input_vraag1)

if vraag1 == "lopen":
    print()
    print(TextColors.WHITE + "Jullie zijn onderweg naar moscow onderschept en gevangen genomen." + TextColors.RESET)
    print(TextColors.RED + "U heeft uw missie niet gehaald" + TextColors.RESET)
    print(TextColors.BLACK + "Einde spel" + TextColors.RESET)



elif vraag1 == "jatten":
    print()
    time.sleep(1.5)
    print(TextColors.WHITE + "U bent bij de stadsgrenzen van moscow aangekomen. " + TextColors.RESET)
    print(TextColors.WHITE + "Hoe gaan jullie binnenkomen? " + TextColors.RESET)
    input_vraag2 = TextColors.BLUE + "Via het riool of blazen jullie de muur op? " + TextColors.RESET + " (riool/opblazen): "
    vraag2 = input(input_vraag2)



    if vraag2 == "riool":
        print("u heeft gekozen voor" ,vraag2)
        time.sleep(1.5)
        print("\nU heeft met het naar binnen trede het alarm af laten gaan en de russen hebben het riool vol laten lopen.")
        print(TextColors.RED + "U heeft verloren, helaas." + TextColors.RESET)


    elif vraag2 == "opblazen":
        print("u heeft gekozen voor" ,vraag2)
        time.sleep(1.5)
        print(TextColors.WHITE + "\nU heeft het bevel geven om de muur op te blazen maar was dat wel een slimme zet?" + TextColors.RESET)
        print(TextColors.WHITE + "omdat U in een oorlogsgebied zit zijn er overal militairen daarodat er zo enorme knal kwam zijn alle eenheden naar jullie positie gegaan." + TextColors.RESET)
        print(TextColors.RED + "U bent nu met uw team in een heftige vuurgevecht gekomen." + TextColors.RESET)
        input_vraag3 = TextColors.BLUE + "Wat gaat u doen?" + TextColors.RESET + " (overgeven/luchtsteun): "
        vraag3 = input(input_vraag3)


        if vraag3 == "overgeven":
            print("\nU heeft gekozen om de witte vlag te heisen en over te geven.")
            print("Jullie zijn krijgsgevangen genomen en zullen nooit meer de buiten wereld te zien krijgen.")
            time.sleep(1.5)
            print(TextColors.RED + "Missie gefaald" + TextColors.RESET)

        elif vraag3 == "luchtsteun":
            print("\nU heeft gekozen om luchtsteun aan te vragen.")
            print("🛩               🛩")
            print(" 🛩            🛩")
            print("   🛩        🛩")
            print("           🛩")
            print("     💥💥💥    ")
            time.sleep(1)
            print("\nU heeft het doel uitgeschakeld en kan weer op weg naar je missie.")
            print("wel tempo maken de vijanden hebben dit namelijk ook gehoord.")
            print(TextColors.WHITE + "\nu bent bij de warehouse gekozen van de tango, hoe wil je binnen komen?" + TextColors.RESET)
            input_vraag4 = TextColors.BLUE + "Wacht je tot je een guard ziet en zo ze pasje steelt, of trap je de deuren in?" + TextColors.RESET + " (stelen/in trappen): " 
            vraag4 = input(input_vraag4)


            if vraag4 == "stelen":
                print("u heeft gekozen voor" , vraag4)
                print("\nDit was niet slim de soldaten zijn heel alert")
                print(TextColors.RED + "verloren" + TextColors.RESET)


            elif vraag4 == "in trappen":
                print("u heeft gekozen voor" , vraag4)
                print("\nStorm naar binnen en voltooi je missie Alfa!!!")
                time.sleep(5)
                print("\nU heeft uw missie behaald gefeliciteerd")


    
    

