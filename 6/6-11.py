#6-11. Cities: Make a dictionary called cities. Use the names of three cities as
#keys in your dictionary. Create a dictionary of information about each city and
#include the country that the city is in, its approximate population, and one fact
#about that city. The keys for each city’s dictionary should be something like
#country, population, and fact. Print the name of each city and all of the information 
#you have stored about it.

cities = {
    'st paul': {
        'population': 300000,
        'state': 'minnesota',
        'fact': 'Experiences 160 f temperature deviation.',
    },
    'milwaukee': {
        'population': 250000,
        'state': 'wisoconsin',
        'fact': 'Baseball team is called the Berwers',
    },
    'san carlos': {
        'population': 145000,
        'state': 'california',
        'fact': 'Interning here',
    }
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tState: {info['state'].title()}")
    print(f"\tFact: {info['fact']}")
    
print("That's all folks!")