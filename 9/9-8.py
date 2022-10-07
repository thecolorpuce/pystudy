"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class User:
    def __init__(self, first_name, last_name, address, age):
        """Create a user, and assign information."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
    
    def describe_user(self):
        """List out information about user."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"\t Address: {self.address}")
        print(f"\tAge: {self.age}")
    
    def greet_user(self):
        """A simple greeting for the user."""
        print(f"Greetings {self.first_name} {self.last_name}!")

class Privileges:
    """An attempt to model privilege levels"""
    
    def __init__(self):
        """Initialize privilege attributes"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for i in self.privileges:
            print(f"{i}")

class Admin(User):
    def __init__(self, first_name, last_name, address, age):
        """Initialize the admin userInerit the items from User"""
        
        super().__init__(first_name, last_name, address, age)
        self.privileges = Privileges()



admin1 = Admin('Riley', 'Abbs', '9 3/4', '28')

admin1.privileges.show_privileges()