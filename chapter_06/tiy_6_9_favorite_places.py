# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-01
# --------------------------------------------------------------------------- #

favorite_places = {
    'nati': ['bogota', 'paris', 'madrid'],
    'dani': ['humacao', 'santa marta'],
    'adolfo': ['seattle', 'barcelona', 'honolulu', 'san juan']
    }

for name, places in favorite_places.items():
    print(f"{name.title()}\'s favorite places are:")
    for place in places:
        print(f"\t {place.title()}")