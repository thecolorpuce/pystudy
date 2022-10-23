"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""
# I'm just going to do this in one program..

import json

filename = 'text_files/10-11.json'

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

print_number(filename)