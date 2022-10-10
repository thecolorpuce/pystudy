file_path = 'text_files/test_file.txt'

with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())