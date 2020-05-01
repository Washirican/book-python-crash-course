# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-01
# --------------------------------------------------------------------------- #

cities = {
    'bogota': {
        'country': 'colombia',
        'population': '7.413 million',
        'fact': 'Is located in a plateau that is 9,000 feet above sea level'
        },
    'seattle': {
        'country': 'united states',
        'population': '744,955',
        'fact': 'The land that is now the city of Seattle has been inhabited '
                'for at least 4,000 years'
        },
    'madrid': {
        'country': 'spain',
        'population': '6.642 million',
        'fact': "The name Madrid comes from the arabic \"magerit\" which "
                "means \"place of many streams\""
        },
    }

for city, city_data in cities.items():
    print(f"Some interesting facts about {city.title()} are: ")
    for category, data in city_data.items():
        print(f"\t{category.title()}: {data.title()}")
    print()





