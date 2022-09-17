"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

lo = True

def ticketPrice(age):
    """Movie ticket prices based on age...
    
    if age <= 3 == Free
    if age >3 && < 12 == $10
    if age > 12 == $15
    ----------------------------------------
    """
    if age <= 3:
        return 0
    elif age > 3 and age <= 12:
        return 10
    else:
        return 15

while lo == True:
    age = int(input("Please enter your age: "))
    price = ticketPrice(age)
    print(f"The ticket is ${price}...")
    cont = input("Would you like another ticket? ('q' to quit)")
    if cont == 'q':
        lo = False
    else:
        continue
