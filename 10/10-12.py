"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

# See 10-11, but I'll post it in here all the same
# Updating this to let the user choose the filename

import json



def get_number():
    """Get the user's favorite number"""
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)

def print_number(filename):
    """Print the user's favorite number"""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        get_number()
    else:
        print(f"{contents}")

filename = input("Where would you like to store this file?")
filename = str(filename) + '.json'

print_number(filename)