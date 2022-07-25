"""Optional argument"""

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name}, {middle_name}, {last_name}"
    else:
        full_name = f"{first_name}, {last_name}" 
    return full_name.title()

musician = get_formatted_name('riley', 'ray', 'asp')
musician2 = get_formatted_name(first_name='riley', last_name='asp')
print(musician)
print(musician2)