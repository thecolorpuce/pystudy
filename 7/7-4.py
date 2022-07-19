prompt = "\nWhat would you like?: "
prompt += "\nEnter 'quit' to end the program. "

active = True

topping = ""

while active:
    topping = input(prompt)
    
    if topping == 'quit':
        active = False
    else:
        print(f"\tWe'll add {topping.title()} to the pie...")
        print("Anything else?")