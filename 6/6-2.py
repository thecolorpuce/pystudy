#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program

fNumber = {'riley': 5,
           'sam': 16,
           'ean': 420,
           'dan': 55,
           'Ash': 16}

for val in fNumber:
    print(f"This is {val.title()}, their favorite number is {fNumber[val]}")
    