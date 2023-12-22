getal = int(input("welke tafel wilt u zien? \n"))

print(f"de tafel van {getal}\n")


for i in range(1, 11):
    resultaat = getal * i

    print(f"{i} x {getal} = {resultaat}")
    