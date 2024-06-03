country = input('Enter a  country: ')  # Add country name
visits = int(input('Enter number of visits to the country: '))  # Number of visits
list_of_cities = eval(input(f'Enter list of cities visited in {country}: '))  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Write the function that will allow new countries to be added to the travel_log.
def add_new_country(country_name, number_of_visits, city_names):
    travel_log.append({"country": country_name, "visits": number_of_visits, "cities": city_names})


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
