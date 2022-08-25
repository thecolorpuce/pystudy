"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

riley_asp = {'first_name': 'riley',
             'last_name': 'asp',
             'age': 28,
             'city': 'chetek'
}

firstName  = riley_asp['first_name']
lastName = riley_asp['last_name']
age = riley_asp['age']
city = riley_asp['city']

print(f"First Name: {firstName.title()}")
print(f"Last Name: {lastName.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")