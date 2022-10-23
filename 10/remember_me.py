import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename , 'w') as f:
    json.dump(username, f)
    print(f"I will remember you {username.title()}")