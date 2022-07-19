#7-5. Movie Tickets: A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.

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
        active = False
    elif age > 12:
        price = 15
        print(f"Your price is ${price}")
        active = False
    else:
        print("Please enter a valid input...")