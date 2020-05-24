# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-23
# --------------------------------------------------------------------------- #
import json


def get_new_favorite_number():
    """Get user's favorite number."""
    favorite_number = input("Whats your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    return favorite_number


def get_stored_favorite_number():
    """Read favorite number from file."""
    filename = 'favorite_number.json'
    with open(filename) as f:
        favorite_number = json.load(f)
    return favorite_number


get_new_favorite_number()

favorite_number = get_stored_favorite_number()
print(f"Your favorite number is {favorite_number}")
