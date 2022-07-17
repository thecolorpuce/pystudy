#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

person0 = {
    'fname': 'Riley',
    'lname': 'Asp',
    'city': 'Chetek'
}

person1 = {
    'fname': 'Sam',
    'lname': 'Dobbs',
    'city': 'Plymouth'
}

person2 = {
    'fname': 'Ean',
    'lname': 'Malchow',
    'city': 'St. Paul'
}

people = [person0, person1, person2]

for person in people:
    fullName = f"{person['fname'].title()} {person['lname'].title()}"
    location = f"{person['city'].title()}"
    
    print(f"{fullName}: {location}")

