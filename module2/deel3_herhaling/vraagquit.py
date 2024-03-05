count = 0

while True:
    user_input = input("? ")
    count += 1

    if user_input == 'quit':
        break

print(f"\nAantal iteraties: {count}")
