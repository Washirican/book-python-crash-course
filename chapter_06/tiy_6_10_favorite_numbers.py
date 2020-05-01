# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-01
# --------------------------------------------------------------------------- #

favorite_number = {
    'dani': [3, 12],
    'nati': [13, 11],
    'michael': [23, 32],
    'larry': [33, 234],
    'damian': [0, 11],
    }

for name, numbers in favorite_number.items():
    print(f"{name.title()}\'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
