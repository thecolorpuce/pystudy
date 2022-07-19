#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
#that do each of the following at least once:

#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nWhat is your age? :"
price = 0

active = True

while active:
    age = input(prompt)
    age = int(age)
    
    if age > 0 and age < 3:
        price = 0
        print(f"\tYour price is ${price}")
        active = False
    elif age >= 3 and age <= 12:
        price = 10
        print(f"\tYour price is ${price}")
    elif age > 12:
        price = 15
        print(f"Your price is ${price}")
        active = False
    elif age == 'quit':
        break
    else:
        print("Please enter a valid input...")