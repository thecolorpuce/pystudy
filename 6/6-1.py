#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person = {'fName': 'Riley',
          'lName': 'Asp',
          'city': 'Chetek'}

print(f"This is {person['fName'].title()}\n")
print(f"Their last name is {person['lName'].title()}\n")
print(f"They're from {person['city'].title()}\n")

print("Thanks for asking!")