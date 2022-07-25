#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
#the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has
#run out of pastrami, and then use a while loop to remove all occurrences of
#'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
#in finished_sandwiches.

sandwichOrders = ['pb&j', 'salami', 'pastrami', 'balogne']
finishedSandwiches = []

for val in sandwichOrders:
    if val == 'pastrami':
        print("All out of pastrami")
    else:
        finishedSandwiches.append(val)

#Print finSan to verify
#Why not loop it though?

for val in finishedSandwiches:
    print(f"Made you a {val.title()} sandwich")
