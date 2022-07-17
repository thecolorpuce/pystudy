#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {'Mississippi': 'America',
          'Nile': 'Egypt',
          'Aral': 'Russia'
          }

#3 for loops to make everything come together here

for key, val in rivers.items():
    print(f"The {key.title()} river runs through {val.title()}.")

for key in rivers.keys():
    print(key)

for val in rivers.values():
    print(val)
