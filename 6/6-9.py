#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.

favoritePlaces = {
    'riley': 'afton state park',
    'sam': 'bad weather brewery',
    'ean': 'badlands',
}

for person, place in favoritePlaces.items():
    print(f"{person.title()}: {place.title()}")