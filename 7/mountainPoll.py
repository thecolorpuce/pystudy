from asyncore import poll


responses = {}

#Set flag for polling true

polling_active = True

while polling_active:
    #prompt for name and response
    name = input("\nWhat is your name?: ")
    response = input("What mountain would you like to climb someday?: ")
    
    #Store the response in a dictionary
    
    responses[name] = response
    
    #Find out if anyone else is taking the poll
    repeat = input("Would anyone else like to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
#Completed polling

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")