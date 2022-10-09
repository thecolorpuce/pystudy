"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, address, age):
        """Create a user, and assign information."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """List out information about user."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"\t Address: {self.address}")
        print(f"\tAge: {self.age}")
    
    def greet_user(self):
        """A simple greeting for the user."""
        print(f"Greetings {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        """Method for incrementing login attempts."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Method for resetting the number of login attempts."""
        self.login_attempts = 0



rileyabbs = User('Riley', 'Abbs', '93/4', 28)

rileyabbs.describe_user()

for i in range(5):
    rileyabbs.increment_login_attempts()

print(f"{rileyabbs.login_attempts}")

rileyabbs.reset_login_attempts()

print(f"{rileyabbs.login_attempts}")