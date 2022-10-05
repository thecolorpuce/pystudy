"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
"""


class Restaurant:
    """A class to model a restaurant"""
    def __init__(restaurant, name, cuisine_type):
        restaurant.name = name
        restaurant.cuisine_type = cuisine_type
        restaurant.number_served = 0
    
    def describe_restaurant(restaurant):
        """A simple description of the restaurant"""
        print(f"{restaurant.name} serves {restaurant.cuisine_type}")
        print(f"\tTotal Customers Served: {restaurant.number_served}")
    
    def open_restaurant(restaurant):
        """Indicates that the restaurant is now open."""
        print(f"{restaurant.name} is now open!")
    
    def set_number_served(restaurant, number):
        """A method for setting the number of people served."""
        if number < 0:
            print("You need to enter a number > 0...")
        else:
            restaurant.number_served = number
    
    def increment_number_served(restaurant, increment):
        """A method for incrementing number of people served."""
        if increment < 0:
            print("Please enter a number > 0...")
        else:
            restaurant.number_served += increment

restaurant = Restaurant('Applebees', 'Shitty American')

print(f"{restaurant.name}")
print(f"{restaurant.cuisine_type}")
print(f"Number Served...{restaurant.number_served}")

restaurant.set_number_served(10)
print(f"Number served...{restaurant.number_served}")

restaurant.increment_number_served(100)
print(f"Number served...{restaurant.number_served}")


restaurant.describe_restaurant()
restaurant.open_restaurant()