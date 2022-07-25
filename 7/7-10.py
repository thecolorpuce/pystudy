#7-10. Dream Vacation: Write a program that polls users about their dream vaca-
#tion. Write a prompt similar to If you could visit one place in the world, where
#would you go? Include a block of code that prints the results of the poll.

responses = {}

poll = True

while poll:
    name = input("What is your name?: ")
    response = input("Where would you like to go?: ")
    
    responses[name] = response
    
    conf = input("Would you like to enter a new location? (Y/N): ")
    
    if conf == 'n':
        poll = False

for name, response in responses.items():
    print(f"Hello {name.title()}. You want to go to {response.title()}")