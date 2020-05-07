# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


def make_sandwich(*ingredients):
    """Function collects as many sandwich ingredients as given"""
    print('\nMaking your sandwich...')
    for ingredient in ingredients:
        print(f'...adding {ingredient}')


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


