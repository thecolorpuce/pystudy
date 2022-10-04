# Start with some designs that need to be printed

unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

# Simulate printing each design, until none are left.
# Move each design to completedModels after printing.

while unprintedDesigns:
    currentDesign = unprintedDesigns.pop()
    print(f"Printing model: {currentDesign}")
    completedModels.append(currentDesign)

# Display all completed models.
print("\nThe following models have been printed: ")
for completedModel in completedModels:
    print(completedModel)