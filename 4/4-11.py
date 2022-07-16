#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
#(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:

pizzas = ['peperoni','pinneapple','supreme','garbage']

friendPizzas = pizzas[:]
friendPizzas.append('sausage')

print("My favorite pizzas are: ")
for val in pizzas:
    print(val)  

print("My friend's favorite pizzas are: ")
for val in friendPizzas:
    print(val)

print("Thank you")


