#5-8. Hello Admin: Make a list of five or more usernames, including the name
#'admin'. Imagine you are writing code that will print a greeting to each user
#after they log in to a website. Loop through the list, and print a greeting to
#each user:

username = 'admin'

if username == 'admin':
    print(f"Hello {username.title()}. Here is a status report")
else:
    print(f"Hello {username.title()}. Welcome to the site!")