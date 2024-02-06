import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
volledige_deck = ['joker', 'joker']

for kleur in kleuren:
    for waarde in waarden:
        volledige_deck.append(f"{kleur} {waarde}")

random.shuffle(volledige_deck)

for i in range(7):
    kaart = volledige_deck.pop(0)
    print(f"Kaart {i + 1}: {kaart}")

overige_kaarten = [f'"{kaart}"' for kaart in volledige_deck]
print(f"\ndeck ({len(volledige_deck)} kaarten): [ {', '.join(overige_kaarten)} ]")
