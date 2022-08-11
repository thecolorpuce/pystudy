"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on 
a sandwich. The function should have one parameter that collects as many items as the 
function call provides, and it should print a summary of the sand- wich that’s being 
ordered. Call the function three times, using a different num- ber of arguments each time.
"""

def sandwich_maker(size, *toppings):
    """Function to sumarize a sandwich"""
    print(f"\nMaking a {size}-inch sandwich with these toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

sandwich_maker(6, 'Lettuce', 'Salami', '12312')

sandwich_maker(12, '1', '2', '3')

sandwich_maker(22, 'asdf', 'qwe', 'zxc')