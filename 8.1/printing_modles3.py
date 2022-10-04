# Only difference here is that I made use of a copy of unprintedDesigns instead of modifying it.

def print_models(unprintedDesigns, completedModels):
    """
    Simulate printing each design, until none are left.
    Move each design to completedModels after printing.
    """
    
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop()
        print(f"Printing model: {currentDesign}")
        completedModels.append(currentDesign)

def show_completed_models(completedModels):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ")
    for completedModel in completedModels:
        print(completedModel)

unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

print_models(unprintedDesigns[:], completedModels)
show_completed_models(completedModels)

print(unprintedDesigns)