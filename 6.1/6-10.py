""" 
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

tracker = 0

favorite_numbers = {'riley': [5, 10, 11],
                    'sam': [42, 44, 46],
                    'ean': [44, 0, 1],
                    'wayne': [42, 11, 12],
                    'Dalinar': [69, 420, 8008]
                    }

for name, number in favorite_numbers.items():
    tracker = tracker + 1
    print(f"This is list number {tracker}:")
    print(f"Showing list {name.title()}...")
    for v in number:
        print(f"\t{v}")