import random
kleuren = ("oranje", "blauw", "groen", "bruin")

amount = int(input("hoeveel m&ms in de zak? "))

zak_gevuld = []

for _ in range(amount):
    wil_kleur = random.choice(kleuren)
    zak_gevuld.append(wil_kleur)



print("Inhoud van de m&ms:", zak_gevuld)





