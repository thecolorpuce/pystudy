#Store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['musheroom', 'extra cheese'],
}

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")