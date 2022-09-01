""" 
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

favorite_places = {
    'minnesota': 'riley',
    'san francisco': 'sam',
    'mississippi': 'gob gob',
}

for k, v in favorite_places.items():
    print(f"{v.title()}'s favorite location is {k.title()}!")