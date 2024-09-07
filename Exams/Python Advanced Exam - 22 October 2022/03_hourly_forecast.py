def forecast(*args):

    sunny_weather = []
    cloudy_weather = []
    rainy_weather = []

    for info in args:

        if info[1] == "Sunny":
            sunny_weather.append(info[0])
        elif info[1] == "Cloudy":
            cloudy_weather.append(info[0])
        elif info[1] == "Rainy":
            rainy_weather.append(info[0])

    result = []

    for sunny in sorted(sunny_weather):
        result.append(f"{sunny} - Sunny")

    for cloudy in sorted(cloudy_weather):
        result.append(f"{cloudy} - Cloudy")

    for rainy in sorted(rainy_weather):
        result.append(f"{rainy} - Rainy")

    return '\n'.join(item for item in result)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))