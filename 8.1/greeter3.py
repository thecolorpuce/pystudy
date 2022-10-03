import myLib as m

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = m.get_formatted_name(f_name, l_name)
    p