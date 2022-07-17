#7-2. Restaurant Seating: Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message 
# saying they’ll have to wait for a table. Otherwise, report that their table 
# is ready

numGuests = input("How many people are in the dinner group?: ")
numGuests = int(numGuests)  

if numGuests > 8:
    print("Sorry, you will have to wait")
else:
    print("your table is ready!")