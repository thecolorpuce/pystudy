#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
#Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet.

pet0 = {
    'species': 'dog',
    'owner': 'riley',
}
pet1 = {
    'species': 'cat',
    'owner': 'ean',
}
pet2 = {
    'species': 'guinea pig',
    'owner': 'dobbs',
}

pets = [pet0, pet1, pet2]

for pet in pets:
    species = f"{pet['species'].title()}"
    owner = f"{pet['owner'].title()}"
    
    print(f"{owner}: {species}")