"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint


class Dice:
    def __init__(self, sides=None):
        """Initialize dice and create a default d6"""
        self.sides = sides
    
    def roll_die(self):
        if self.sides == '':
            self.sides = 6
        outcome = randint(1, self.sides)
        return f"You rolled a {outcome} out of {self.sides}!"

game1 = Dice(10)
game2 = Dice(20)

for i in range(10):
    print(game1.roll_die())

print('\n' + '#' * 40 + '\n')

for i in range(10):
    print(game2.roll_die())