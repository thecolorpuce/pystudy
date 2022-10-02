"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

def describe_city(city, country):
    """Print a simple sentance city in country"""

    out = f"{city.title()} is in {country.title()}"
    return out

list = []

list.append(describe_city('woodbury', 'united states'))
list.append(describe_city('woodbury2', 'united states2'))
list.append(describe_city('woodbury3', 'united states3'))

for i in list:
    print(i)
