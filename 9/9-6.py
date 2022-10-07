"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
    """A class to model a restaurant"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """A simple description of the restaurant"""
        print(f"{self.name} serves {self.cuisine_type}")
    
    def open_restaurant(self):
        """Indicates that the restaurant is now open."""
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
    """A stimple model of an icecream stand"""
    
    def __init__(self, name, cuisine_type):
        """Initialize the Icecreamstand"""
        super().__init__(name, cuisine_type)
        self.flavors = ['vanila', 'chocolate', 'mint']
    
    def displayFlavor(self):
        for i in self.flavors:
            print(f"{i}")

example1 = IceCreamStand('riley stand', 'Ice Cream')

print(example1.displayFlavor())