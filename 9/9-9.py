"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
"""

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model  
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        long_name+= f"\nThe gas tank is {self.gas_tank}% full."
        return long_name

    def fill_gas_tank(self):
        """Fill the gas tank"""
        self.gas_tank = 100
        
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("Please provide a value greater than 0.")
        else:
            self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize all attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(Car):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need  a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self.capacity = 100
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size  == 75:
            print("Upgrading battery size...\n")
            self.battery_size = 100
        else:
            print("Battery is already upgraded...\n")

car1 = ElectricCar('tesla', 'model 3', 2019)

car1.battery.get_range()
car1.battery.upgrade_battery()
print("\n\n")
car1.battery.get_range()