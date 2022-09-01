#This is showing accepting numerical inputs

age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You have to pay taxes now.")
else:
    print("You don't have to pay taxes.")