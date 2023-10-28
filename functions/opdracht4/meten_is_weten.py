
def compare_numbers(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return "Beide getallen zijn even groot"
    elif nr1 > nr2:
        return f"Maximum: {nr1} en minimum: {nr2}"
    else:
        return f"Maximum: {nr2} en minimum: {nr1}"

# Vraag de gebruiker om twee gehele getallen in te voeren
while True:
    try:
        a = int(input("Voer het eerste gehele getal (a) in: "))
        break
    except ValueError:
        print("Invoer ongeldig, voer een geheel getal in alstublieft!")
        
while True:
    try:
        b = int(input("Voer het tweede gehele getal (b) in: "))
        break
    except ValueError:
        print("Invoer ongeldig, voer een geheel getal in alstublieft!")


#output van de grote
result = compare_numbers(a, b)
print(result)
