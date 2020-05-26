# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-25
# --------------------------------------------------------------------------- #
# Try it yourself exercise 11-1: City, Country


def city_country(city_name, country_name, population=''):
    """Return neatly formatted string containing City, Country and
    population"""

    if population:
        formatted_string = f"{city_name.title()}, {country_name.title()} - " \
                           f"population {population}"
    else:
        formatted_string = f"{city_name.title()}, {country_name.title()}"

    return formatted_string

