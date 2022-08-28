""" 
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary
"""


major_rivers = {
    'nile': 'egypt',
    'mississippi': 'US',
    'styx': 'greece',
}

for k, v in major_rivers.items():
    print(f"\nThe {k.title()} runs through {v.title()}.")

print("\n")
print("The included rivers are:")

for k in set(major_rivers.keys()):
    print(f"{k.title()}")

print("***************************************")
print("\n")
print("The countries included in this list are:")

for k in set(major_rivers.values()):
    print(f"{k.title()}")