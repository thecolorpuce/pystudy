from more_itertools import first


def get_formatted_name(first_name, last_name):
    """Return a full name, newtly formatted"""
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a formatted name with optional middle name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person