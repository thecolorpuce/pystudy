from lib2to3.pgen2.tokenize import generate_tokens


def greet_users(names):
    """Print a simple greeting for each user in the list"""
    
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['riley', 'sirus', 'thecolorpuce', 'aspkicker']

greet_users(usernames)