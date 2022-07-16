places = ['Minnesota', 'Colorado', 'Oregon', 'Montana', 'California']

print("List in original order")
print(places)

print("list in alphabetical order")
print(sorted(places))

print("List in reverse order")
print(sorted(places, reverse=True))

print("changing the actual list to print in reverse order")
places.sort(reverse=True)           
print(places)



print("Changing the list to be back within its normal order")
places.sort()
print(places)
