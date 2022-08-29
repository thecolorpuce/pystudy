""" 
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
people = []

riley_asp = {'first_name': 'riley',
             'last_name': 'asp',
             'age': 28,
             'city': 'chetek'
}

sam_dobs = {
    'first_name': 'sam',
    'last_name': 'dobs',
    'age': 28,
    'city': 'phoenix',
}

ean_malchow = {
    'first_name': 'ean',
    'last_name': 'malchow',
    'age': 25,
    'city': 'st.paul',
}

people = [riley_asp, sam_dobs, ean_malchow]

for v in people:
    print(f"{v['first_name'].title()} {v['last_name'].title()}")
    print(f"\tAge: {v['age']}")
    print(f"\tCity: {v['city'].title()}")