""" 
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""

favorite_numbers = {'riley': 5,
                    'sam': 69,
                    'ean': 420,
                    'wayne': 42,
                    'Dalinar': 743}

for name, number in favorite_numbers.items():
    print(f"{name.title()}: {number}")