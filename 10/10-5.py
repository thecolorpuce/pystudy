"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'text_files/likes_programming.txt'
asking = True

with open(filename, 'a') as file_object:
    while asking is True:
        print("Reasons we like programming!")
        reason = input("Reason:  ")
        if reason != '':
            print(f"{reason}!")
            file_object.write(reason.title())
        else:
            print("Thanks for sharing!")
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