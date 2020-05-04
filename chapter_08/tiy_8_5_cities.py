# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-03
# --------------------------------------------------------------------------- #


def describe_city(city, country='united states'):
    print(f'\n{city.title()} is in {country.title()}.')


if __name__ == '__main__':
    describe_city('seattle')
    describe_city('new york', 'united states')
    describe_city('madrid', 'spain')
