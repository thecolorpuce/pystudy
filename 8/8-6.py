"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned."""

def city_country(city, country):
    """Neatly format a city and country"""
    output = f"{city}, {country}"
    return output.title()

while True:

    print("\nPlease enter a city and country")
    print("Press 'q' to quit at any time")

    city = input("City: ")
    if city == 'q':
        break

    country = input("Country: ")
    if country == 'q':
        break
    
    formattedOut = city_country(city, country)
    print(f"{formattedOut}")

