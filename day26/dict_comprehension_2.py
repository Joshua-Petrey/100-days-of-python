#convert temps in weather_c to farenhiet and place them in a new dict using dict somprehension

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = { day: round((celsius * (9/5) + 32), 1) for day, celsius in weather_c.items() }
print(weather_f)