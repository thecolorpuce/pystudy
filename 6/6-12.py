#6-12. Extensions: We’re now working with examples that are complex enough
#that they can be extended in any number of ways. Use one of the example programs 
#from this chapter, and extend it by adding new keys and values, changing the 
#context of the program or improving the formatting of the output. 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'rasp': {
        'first': 'riley',
        'last': 'asp',
        'location': 'san carlos'
    },
    
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")