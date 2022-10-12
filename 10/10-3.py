"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

filename = 'text_files/guest.txt'
asking = True

with open(filename, 'a') as file_object:
    while asking is True:
        again = input("Would you like to add a name (y/n)?")
        if again == 'y':
            new_name = input("Please Enter a name: ")
            file_object.write(new_name + '\n')
            continue
        else:
            print("Thank you!")
            asking = False
            break
    file_object.close()


file_string = ''
with open(filename, 'r') as file_object:
    print("The following information is in the file...")
    lines = file_object.readlines()
    for line in lines:
        file_string += line.strip()
    file_object.close()
    print(file_string)