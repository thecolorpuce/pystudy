def printModels(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed moodels after printing
    """
    while unprinted_designs:
        currentDesign = unprinted_designs.pop()
        print(f"Print model: {currentDesign}")
        completed_models.append(currentDesign)

def showCompletedModels(completed_models):
    """
    Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completedModel in completed_models:
        print(completedModel)

unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

printModels(unprintedDesigns, completedModels)
showCompletedModels(completedModels)