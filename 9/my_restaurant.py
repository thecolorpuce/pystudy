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