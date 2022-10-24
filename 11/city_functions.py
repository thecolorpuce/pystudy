def formatted_city(city, country):
    """Return a formatted city and country 'Minneapolis, USA'"""
    formatted_name = f"{city}, {country}"
    return formatted_name.title()

def formatted_city_population(city, country, population=None):
    """Same as formatted city, but with optional pop.
    Didn't want to get rid of formatted city as it is a part of other
    parts of my study.
    """
    if population:
        formatted_name = f"{city}, {country} | Population: {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()