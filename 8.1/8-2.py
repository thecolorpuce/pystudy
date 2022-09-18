"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

def favorite_book(title):
    """Print a message using the title parameter"""
    print(f"My favorite book is {title.title()}")

#I actually didn't realize you could nest input like this. Pretty neat.
favorite_book(input("Please enter your favorite book: "))