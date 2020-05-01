# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-01
# --------------------------------------------------------------------------- #

dog_0 = {
    'breed': 'labrador',
    'name': 'jack',
    'age': 13,
    }


dog_1 = {
    'breed': 'boston terrier',
    'name': 'lola',
    'age': 8,
    }


dog_2 = {
    'breed': 'golder retriever',
    'name': 'kaya',
    'age': 6,
    }

dogs = [dog_0, dog_1, dog_2]

for dog in dogs:
    print(f"{dog['name'].title()} is a {dog['breed'].title()} and is "
          f"{dog['age']} years old.")

