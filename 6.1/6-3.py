""" 
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {'word1': 'To be 1',
            'word2': 'To be 2',
            'word3': 'To be 3',
            'word4': 'To be 4',
            'word5': 'To be 5'
            }

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")

#Next is looping through a dictionary. Definitely could use a refresh there