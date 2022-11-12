country_names = input().split(', ')
capital_cities = input().split(', ')

dictionary = {country_names[index]: capital_cities[index] for index in range(len(country_names))}
for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
