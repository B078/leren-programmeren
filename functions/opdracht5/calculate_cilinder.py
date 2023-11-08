import math
from test_lib import test, report

#funtion
def calculate_cilinder_content(diameter, hoogte):
    straal = diameter / 2
    inhoud = math.pi * straal**2 * hoogte
    return round(inhoud, 1)

# Testlijstje
test_data = [
    (8.0, 5.0, 251.3),
    (11.0, 7.0, 665.2),
    (18.0, 7.0, 1781.3),
    (15.0, 2.0, 353.4),
    (0.0, 6.0, 0.0)
]
#de nummertje bij de volgende waarde
for diameter, hoogte, verwachte_inhoud in test_data:
    berekende_inhoud = calculate_cilinder_content(diameter, hoogte)
    test(f'Diameter {diameter}, Hoogte {hoogte}', verwachte_inhoud, berekende_inhoud)

report()
