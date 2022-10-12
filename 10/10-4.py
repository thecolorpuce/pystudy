"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = 'text_files/guest_book.txt'
asking = True

with open(filename, 'a') as file_object:
    while asking is True:
        print("Welcome to the Guestbook!")
        name = input("Please enter your name:  ")
        if name != '':
            print(f"Thanks for coming {name.title()}!")
            file_object.write(name.title())
        else:
            print("No one there?")
            asking = False
            
    file_object.close()


file_string = ''
with open(filename, 'r') as file_object:
    print("The following information is in the file...")
    lines = file_object.readlines()
    for line in lines:
        file_string += line.strip()
    file_object.close()
    print(file_string)