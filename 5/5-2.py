#5-2. More Conditional Tests: You don’t have to limit the number of tests you
#create to ten. If you want to try more comparisons, write more tests and add
#them to conditional_tests.py. Have at least one True and one False result for
#each of the following:

#Test for equality and inequality with strings

car1 = 'subaru'
car2 = 'audi'

print("is car 1 == 'subaru'?")
print(car1  == 'subaru')

print("\nis car 2 == 'subaru'?")
print(car2 == car1) #Why not just do this here?

print("\n---------------------------------------------------------------\n")

#Test using the lower() method
#Using the same stuff, but lightly altered. 

car1 = 'Subaru'

print(f"Is {car1.lower()} == 'Subaru'?")
print(car1.lower()  == 'Subaru')

print(f"\nIs {car1.lower()} == 'subaru'?")
print(car1.lower() == 'subaru')

print("\n---------------------------------------------------------------\n")

#Numerical tests involving equality and inequality, greater than and
#less than, greater than or equal to, and less than or equal to

n1 = 1
n2 = 10
n3 = 100

#Equal to

print(f"is {n1} == to '1'?")
print(n1 == 1)

print("\n")

print(f"is {n1} != {n2}?")
print(n1 == n2)

print("\n")

#less than / greater than

print(f"is {n1} < {n2}?")
print(n1 < n2)

print("\n")

print(f"Is {n1} > {n2}?")   
print(n1 > n2)

print("\n")

print(f"Is {n3} > {n2}?")
print(n3 > n2)

print("\n")

print(f"Is {n2} > {n3}?")
print(n2 > n3)

print("\n---------------------------------------------------------------\n")

#Using AND and OR keywords

print(f"Is {n3} > {n1} and {n2}")

if n3 > n1 and n2:
    print(True)

if n2 > n1 or n3:
    print(True)

print("\n---------------------------------------------------------------\n")

#Test if an item is in a list

list = ['it1','it2','it3','it4']
item = 'it2'
item2 = 'it5'

print("Is it2 in the list?")
if item in list:
    print(True)
    
print("Is it5 in list?")
if item2 not in list:
    print(False)

#That's that.