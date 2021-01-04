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


def add_new_country(country_visited, number_of_visits, cities_visited_list):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = number_of_visits
    new_country["cities"] = cities_visited_list

    travel_log.append(new_country)

    if number_of_visits > 1:
        print(f"You have visited {country_visited} {number_of_visits} times")
    else:
        print(f"You have visited {country_visited} {number_of_visits} once")
        print(travel_log[-1])

add_new_country('Russia', 3, ['lorain', 'lima', 'sandusky'])
