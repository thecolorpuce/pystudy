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

print("Good news, there's more room now")

guestList.insert(0, 'Wisconsin')
guestList.insert(2, 'Minnesota')
guestList.append('Last')

print(guestList)


print("JK fuckers! Only two of you can sit!")

ditchedGuest = guestList.pop()
print(f"\n Sorry {ditchedGuest.title()}, no room!")
ditchedGuest = guestList.pop()
print(f"\n Sorry {ditchedGuest.title()}, no room!")
ditchedGuest = guestList.pop()
print(f"\n Sorry {ditchedGuest.title()}, no room!")
ditchedGuest = guestList.pop()
print(f"\n Sorry {ditchedGuest.title()}, no room!")

print(guestList)