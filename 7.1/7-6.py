"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value
"""

"""selectedToppings = []
loop = True
print("Input 'quit' to quit at any time...")

while loop is True:
    topping = input("\nPlease enter a topping: ")
    if topping == 'quit':
        break
    else:
        selectedToppings.append(topping)

for i in selectedToppings:
    print(f"{i.title()}")"""

selectedToppings = []
loop = 0
print("Input 'quit' to quit at any time...")

while loop < 3:
    topping = input("Please enter a topping: ")
    if topping == 'quit':
        break
    else:
        loop += 1
        selectedToppings.append(topping)

for i in selectedToppings:
    print(f"{i.title()}")