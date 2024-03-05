pizzas = [
    {'naam': 'Margherita', 'diameter_cm': 30},
    {'naam': 'Pepperoni', 'diameter_cm': 35},
    {'naam': 'Hawaiian', 'diameter_cm': 40},
    {'naam': 'Vegetarian', 'diameter_cm': 32},
    {'naam': 'Meat Lovers', 'diameter_cm': 38},
    {'naam': 'Mushroom', 'diameter_cm': 33},
    {'naam': 'BBQ Chicken', 'diameter_cm': 36},
    {'naam': 'Four Cheese', 'diameter_cm': 42},
    {'naam': 'Seafood', 'diameter_cm': 37},
    {'naam': 'Spinach and Feta', 'diameter_cm': 34}
]


for pizza in pizzas:
    print(f"Naam Pizza: {pizza['naam']}, de diameter is {pizza['diameter_cm']}")


grootste_pizza = max(pizzas, key=lambda pizza: pizza['diameter_cm'])
print(f"De grootste pizza is {grootste_pizza['naam']} met een diameter van {grootste_pizza['diameter_cm']} cm.")


gesorteerde_pizzas = sorted(pizzas, key=lambda pizza: pizza['diameter_cm'])
print('\n')
for pizza in gesorteerde_pizzas:
    print(f"Naam: {pizza['naam']}, Diameter: {pizza['diameter_cm']} cm")