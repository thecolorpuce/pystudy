"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""

from random import choice


lottery = (1, 2, 3, 4, 5, 6, 7, 8, 'r', 'i', 'l', 'e', 'y')
winning_ticket = []
winner = False

for i in range(4):
    winning_ticket.append(choice(lottery))

print(f"Any ticket matching {winning_ticket} wins a prize")

my_ticket = []
increment = 0

while winner == False:
    my_ticket.clear()
    for i in range(4):
        my_ticket.append(choice(lottery))
    if my_ticket == winning_ticket:
        print('#'*40)
        print(f"It took {increment} tries\n")
        print(f"Your Ticket: {my_ticket}")
        print(f"Winning Ticket: {winning_ticket}\n")
        print('#'*40)
        winner = True
        break
    else:
        increment += 1
        print(f"Try: {increment}")
        print(f"{my_ticket}")
        print(f"{winning_ticket}")
        #time.sleep(0.05)

