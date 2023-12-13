auto_list = []  

for _ in range(3):
    auto = {}  
    auto['merk'] = input("Voer het automerk in voor auto: ")
    auto['model'] = input("Voer het model in voor auto: ")
    auto['prijs'] = input("Voer de prijs in voor auto: ")
    auto_list.append(auto)

for a in auto_list:
    print(a)
