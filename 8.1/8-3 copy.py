"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(text, size='large'):
    """A shirt that prints out the size and the text"""

    return f"Making a Size:{size.title()} shirt with the text:{text}"

shirts = []

shirts.append(make_shirt("I love Python."))
shirts.append(make_shirt(size='Small', text="I'm going to shit yourself!"))

for i in shirts:
    print(i)