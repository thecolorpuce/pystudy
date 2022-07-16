guestList = ['riley', 'ray', 'asp']

print(f"\n Welcome to Dinner {guestList[0].title()}")
print(f"\n Welcome to Dinner {guestList[1].title()}")
print(f"\n Welcome to Dinner {guestList[2].title()}")

print(f"\n Looks like {guestList[1].title()} can't make it to dinner")

del guestList[1]
guestList.insert(1,'rey')
print(f"New List {guestList[0].title()}")
print(f"New List {guestList[1].title()}")
print(f"New List {guestList[2].title()}") 