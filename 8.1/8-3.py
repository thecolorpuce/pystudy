"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(size, text):
    """A shirt that prints out the size and the text"""

    return f"Making a Size:{size.title()} shirt with the text:{text}"

print(make_shirt('M', "I'm going to shit yourself!"))