""" 
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

tracker = 0

cities = {
    'st paul': {
        'country': 'united states',
        'population': 250000,
        'fact': 'chris lyndall is a prophet here'
    },
    'chetek': {
        'country': 'united states',
        'population': 6500, 
        'fact': "I've lived here for years, and don't know the names of the lakes."
    },
    'iwakuni': {
        'country': 'japan',
        'population': 200000,
        'fact': "The Marine Corps base is pretty lame."
    },
}

for city, info in cities.items():
    print(f"This is {city.title()}:")
    for k, v in info.items():
        print(f"\tFacts: {k.title()}:")
        print(f"\t\t{v}")