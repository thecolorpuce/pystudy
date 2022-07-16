#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
#independent if statements that check for certain fruits in your list.

fav = ['apple','pear','orange']

selection = '' 

for val in fav:
    if val == 'apple':
        selection = val
        print(f"\nYou really like {val.title()}s")
    elif val == 'grape':
        selection = val
        print(f"\nYou really like {val.title()}s")
    elif val == 'pear':
        selection = val
        print(f"\nYou really like {val.title()}s")
    elif val == 'banana':
        selection = val
        print(f"\nYou really like {val.title()}s")
    elif val == 'orange':
        selection = val
        print(f"\nYou really like {val.title()}s")
    else:
        print("It would seem that this is fruitless")