#Variation on a simple function for printing a greeting

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

for val in range(10):
    greet_user('riley')