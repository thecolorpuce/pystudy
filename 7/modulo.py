#Some modulo shenanigans
#Useful, but my dumb brain is dumb

number = input("Enter a number, and we'll see if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")