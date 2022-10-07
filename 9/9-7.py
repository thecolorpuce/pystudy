"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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

class Admin(User):
    def __init__(self, first_name, last_name, address, age):
        """Initialize the admin userInerit the items from User"""
        
        super().__init__(first_name, last_name, address, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for i in self.privileges:
            print(f"{i}")


admin1 = Admin('Riley', 'Abbs', '93/4', 28)

admin1.show_privileges()
admin1.describe_user()