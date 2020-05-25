# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-25
# --------------------------------------------------------------------------- #

import json


def get_stored_favorite_number():
    """Read favorite number from file."""
    filename = 'favorite_number.json'

    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_favorite_number():
    """Get user's favorite number."""
    favorite_number = input("Whats your favorite number? ")
    filename = 'favorite_number.json'

    # NOTE (D. Rodriguez 2020-05-25): No need for try/except block since
    #  if filename does not exist it will be created
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    return favorite_number


get_new_favorite_number()

your_favorite_number = get_stored_favorite_number()
print(f"Your favorite number is {your_favorite_number}")

