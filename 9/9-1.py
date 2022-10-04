"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""

class Restaurant:
    """A class to model a restaurant"""
    def __init__(restaurant, name, cuisine_type):
        restaurant.name = name
        restaurant.cuisine_type = cuisine_type
    
    def describe_restaurant(restaurant):
        """A simple description of the restaurant"""
        print(f"{restaurant.name} serves {restaurant.cuisine_type}")
    
    def open_restaurant(restaurant):
        """Indicates that the restaurant is now open."""
        print(f"{restaurant.name} is now open!")

restaurant = Restaurant('Applebees', 'Shitty American')

print(f"{restaurant.name}")
print(f"{restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()