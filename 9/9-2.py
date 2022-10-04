"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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


restaurant1 = Restaurant('Applebees', 'Shitty American')
restaurant2 = Restaurant('Akita', 'Sushi')
restaurant3 = Restaurant('CoCos', 'Japanese Curry')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()