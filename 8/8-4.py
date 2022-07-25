"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""

def make_shirt(message='I love Python', size='L'):
    print(f"The shirt will say '{message}' and be a size '{size.title()}'")

make_shirt('Welcome to Python!')
make_shirt()