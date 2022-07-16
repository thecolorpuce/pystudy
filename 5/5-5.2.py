#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
#else chain.

alienColor = 'yellow'
points = []

if alienColor == 'green':
    points.append(5)
    print("5 points!")
elif alienColor == 'yellow':
    points.append(10)
    print("10 points!")
else:
    points.append(15)
    print("15 points!")
print(points)