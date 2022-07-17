height = input("How tall are you, in inches? ")
height = int(height)

if height >=48:
    print("\nYou're tall enough to ride!")
elif height <48:
    print("\nSorry, you're not tall enough to ride.")
else:
    print("Please use a valid input")