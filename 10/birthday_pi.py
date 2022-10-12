filename = 'pi_digits_2.txt'

with open (filename) as file_object:
    lines = file_object.readlines()

pi_string = '' 
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday (mmddyy): ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    