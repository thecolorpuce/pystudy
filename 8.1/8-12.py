"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""

def make_sandwich(*ingredients):
    """Prints the ingredients of a sandwich out"""
    print("We're makeing a sandwich with the following ingredients...")
    for ingredient in ingredients:
        print(f"\t- {ingredient.title()}")


make_sandwich('salami')
make_sandwich('ham', 'mustard', 'cheese')
make_sandwich('pickeles', 'icecream')