num_lijst = int(input("Hoeveel lijstjes? "))

all_lijst = []

for i in range(num_lijst):
        
        lijst_length = int(input(f"Hoeveel in lijst {i + 1}? "))

        current_lijst = [0] * lijst_length

        all_lijst.append(current_lijst)

for lijstje in all_lijst:
        print(lijstje)

   
