#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
#so each person can have more than one favorite number. Then print each 
#person’s name along with their favorite numbers.

fNumber = {
    'riley': [5,10],
    'sam': [1,2,3,4,5],
    'ean': [420],
    'dan': [77,9],
    'Ash': [7,5]
}

for name, numbers in fNumber.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")