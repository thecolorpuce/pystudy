#7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
#ous sandwiches. Then make an empty list called finished_sandwiches. Loop
#through the list of sandwich orders and print a message for each order, such
#as I made your tuna sandwich. As each sandwich is made, move it to the list
#of finished sandwiches. After all the sandwiches have been made, print a
#message listing each sandwich that was made.

sandwichOrders = ['pb&j', 'salami', 'pastrami', 'balogne']
finishedSandwiches = []

for val in sandwichOrders:
    print(f"\nI made you a {val.title()} sandwich")
    finishedSandwiches.append(val)

#print the list to confirm
print(finishedSandwiches)
