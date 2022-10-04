"""
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
"""

import printing_functions as pf

unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

pf.print_models(unprintedDesigns[:], completedModels)
pf.show_completed_models(completedModels)

print(unprintedDesigns)