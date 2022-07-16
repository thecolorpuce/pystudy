#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['peperoni','pinneapple','supreme',]

for pizza in pizzas:
    #print a simple sentance for each pizza
    print(f"I like {pizza.title()}")
    
print(f"\nI really enjoy pizza! \n")

print(f"I enjoy {pizzas[0].title()}")
print(f"I also enjoy {pizzas[1].title()}")
print(f"Let's not forget about {pizzas[2].title()}")