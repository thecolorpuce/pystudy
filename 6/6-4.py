#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When
#you’re sure that your loop works, add five more Python terms to your glossary.
#When you run your program again, these new words and meanings should
#automatically be included in the output.

glossary = {'loop': 'Repeating a process for a number of itterations',
            'string': 'A string of characters. Not integers',
            'tuple': 'A list with immutable values',
            'dictionary': 'A list with keys, and values assigned to said keys',
            'index': 'What we use to specify the location within a list',
            'ide': 'Integraded Development Environment',
            'language': 'What the programming flavor be',
            'key': 'The main attribute in a definition',
            'value': 'The value of the main attribute associated with said key',
            'word': 'definition3'}

print("Here are some definitions!\n")

for key, value in glossary.items():
    print(f"{key.title()}: {value}")