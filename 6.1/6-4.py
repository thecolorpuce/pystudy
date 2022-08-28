"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

glossary = {'word1': 'To be 1',
            'word2': 'To be 2',
            'word3': 'To be 3',
            'word4': 'To be 4',
            'word5': 'To be 5',
            'word6': 'To be 6',
            'Word7': 'To be 7',
            'Word8': 'To be 8',
            'Word9': 'To be 9',
            'Word10': 'To be 10',
            }

for k, v in glossary.items():
    print(f"{k.title()}: {v}\n")