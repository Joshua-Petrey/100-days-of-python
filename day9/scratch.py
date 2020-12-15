my = {
	'bug': "unexpected errors in a program",
	'function': "A reusable piece of code"}

print(my.get('bug'))
print(my['function'])

my["loop"] = "Allows us to do domething repeatedly"

for key in my:
	print(key,": ", my[key])

# Dictionaries can change mutate each other.
# original can change copy, copy can change original
# The copies are shallow
empty = {}
my = empty
empty["key"] = "some value"
print(my['key'])
del my['key']
# print(empty['key'])


# list in dict

cities_i_traveled = {
	"USA" : ["New York", "Miami", "El Paso"],
	"Canada": ["Toronto", "London", "Ottawa"]
}
print(cities_i_traveled["USA"][2])


# dict in dict
travel_log = {
	"USA" : {
		"New York": 2,
		"Miami": 6,
		"El Paso": 9},
	"Canada": {
		"Toronto": 1,
		"London": 4, 
		"Ottawa": 2}
}
print(travel_log['Canada']['London'])

# list in dict in dict
travel_log2 = {
	"USA" : {'cities_visited': ["Elyria", "Lorain", "Lima"],
			 'total_visits': 12 }
}
print(travel_log2['USA']['total_visits'])


# dict in list
travel_log3 = [
		{'country': 'usa',
		'cities_visited': ["Elyria", "Lorain", "Lima"],
		"total_visits": 15} ,
		{'country': 'Canada',
		'cities_visited': ["Toronto", "London", "Ottawa"],
		"total_visits": 10}

	
]
print(travel_log3[0]['cities_visited'])