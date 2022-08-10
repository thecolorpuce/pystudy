"""A function to make a pizza.
Food is always a great example"""

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')