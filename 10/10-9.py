"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""
def read_text(filename):
    """Return a list with the contents of the file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        names = contents.split()
        for name in names:
            print(name)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    read_text(filename)
