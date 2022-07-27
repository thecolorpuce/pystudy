#Start with some designs that need to be printed
from locale import currency


unprintedDesigns = ['phone case', 'robot pendant', 'dodechedron']
completeModels = []

#simulate printing each design until none are left
#move each design to complete_models after printing

while unprintedDesigns:
    currentDesign = unprintedDesigns.pop()
    print (f"Printing model: {currentDesign}")
    completeModels.append(currentDesign)
    
#Display Completed Models

print("\nThe following models have been printed: ")

for completeModel in completeModels:
    print(completeModel)