"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""


results = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    location = input("What is your dream vacation location? ")
    results[name] = location
    cont = input("Would you like to let another answer? (yes/no): ")
    if cont == 'no':
        poll_active = False
    else:
        continue

for i, v in results.items():
    print(f"{i} Would like to go to {v}")
