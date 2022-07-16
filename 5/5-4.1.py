#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
#write an if-else chain.

alienColor = 'red'
points = []

if alienColor == 'green':
    points.append(5)
    print("5 points!")
elif alienColor != 'green':
    points.append(10)
    print("10 points!")
    
print(points)