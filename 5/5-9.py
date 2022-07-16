#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
#not empty.

username = 'Riley'

if username == 'admin':
    print(f"Hello {username.title()}. Here is a status report")
elif username == '':
    print("We need to find a user!")
else:
    print(f"Hello {username.title()}. Welcome to the site!")