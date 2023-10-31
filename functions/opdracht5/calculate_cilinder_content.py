import math
#funtion
def inhoud(hoogte_cilinder: float, diameter: float) -> float:
    straal = diameter / 2
    inhoud = math.pi * (straal ** 2) * hoogte_cilinder #Inhoud = (diameter/ 2) x (diameter/ 2) x Pi x hoogte1
    return inhoud 
    
#input
while True:
    try:
        hoogte_cilinder = float(input("Wat is de hoogte van de cilinder? "))
        diameter = float(input("Wat is de diameter van de cilinder? "))
        break
    except ValueError:
        print("U heeft 1 van de vragen niet met een getal beantwoord")

cilinder_inhoud = inhoud(hoogte_cilinder, diameter)

print(f"De inhoud van de cilinder is: {round(cilinder_inhoud, 1)}") #output 


