with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
# rstrip removes the blank line produced by the 'read' function