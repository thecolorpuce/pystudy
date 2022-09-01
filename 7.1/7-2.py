""" 
7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message 
saying they’ll have to wait for a table. Otherwise, report that their table is ready
"""

people_num = input("How many people will be dining tonight? ")
people_num = int(people_num)

if people_num > 8:
    print("You will have to wait for a table..")
else:
    print("Your table is ready!")