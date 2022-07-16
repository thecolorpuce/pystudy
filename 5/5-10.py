#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.

currentUsers = ['usr1','usr2','usr3','usr4','usr5']
upperUsers = [val.upper() for val in currentUsers]

newUsers = ['nusr1','nusr2','nusr3','nusr4','usr5','USR4']

for val in newUsers:
    if val in currentUsers or upperUsers:
        print(f"You already exist {val.title()}")
    else:
        print(f"Welcome to the site {val.title()}!")