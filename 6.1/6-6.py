#6-6. Polling: Use the code in favorite_languages.py (page 97).
#•	 Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#•	 Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.

take_poll = ['riley', 'jim', 'blake', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for v in take_poll:
    print(f"{v.title()}")
    
    for k in favorite_languages.keys():
        if v == k:
            print(f"Thank you for taking the poll {v.title()}!")
        else:
            print(f"Please take the poll {v.title()}!")
            break