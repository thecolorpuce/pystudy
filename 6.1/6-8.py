""" 
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

tracker = 0

pet1 = {
    'animal': 'dog',
    'owner': 'greg',
}

pet2 = {
    'animal': 'cat',
    'owner': 'riley',
    'name': 'bean',
}

pet3 = {
    'animal': 'rat',
    'owner': 'tanner',
    'name': 'sigfried',
}

pets = [pet1, pet2, pet3]

for v in pets:
    tracker = tracker + 1
    print(f"Entering loop {tracker}...")
    for key, value in v.items():
        print(f"key: {key}, Value {value}")