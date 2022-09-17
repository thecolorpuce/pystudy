"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

selectedToppings = []
loop = True
print("Input 'quit' to quit at any time...")

while loop is True:
    topping = input("\nPlease enter a topping: ")
    if topping == 'quit':
        break
    else:
        selectedToppings.append(topping)

for i in selectedToppings:
    print(f"{i.title()}")