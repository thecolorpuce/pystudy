def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name}, {middle_name}, {last_name}"
    else:
        full_name = f"{first_name}, {last_name}" 
    return full_name.title()

#Here be a infinite loop
while True:
    print("\nPlease tell me your name: ")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    
    formattedName = get_formatted_name(fName, lName)
    
    print(f"\nHello, {formattedName}!")