# I will not be making use of any libs just to make reading these examples easier
# Of course until we get to making libraries

"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""

def city_country(city, country):
    """Take the input of a city and a country
    
    return a formatted output "city, country"
    """
    
    return f"{city.title()}, {country.title()}"

print(city_country('minneapolis', 'united states'))