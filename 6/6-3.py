#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.

glossary = {'loop': 'Repeating a process for a number of itterations',
            'string': 'A string of characters. Not integers',
            'tuple': 'A list with immutable values',
            'dictionary': 'A list with keys, and values assigned to said keys',
            'index': 'What we use to specify the location within a list'}

print("Here are some definitions!\n")

for val in glossary:
    print(f"{val.title()}: {glossary[val]}\n")