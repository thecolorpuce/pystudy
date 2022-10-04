"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
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


user0 = User('riley', 'asp', '952A 9 3/4', '28')
user1 = User('sam', 'barrel', '123 address', '28')
user2 = User('ean', 'mailroom', '420 blaze it', '26')

list = [user0, user1, user2]

for i in list:
    i.describe_user()
    print("\n")
    i.greet_user()