# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #
from restaurant import Restaurant


restaurant = Restaurant('amaro bistro', 'italian')

print(f'\n{restaurant.restaurant_name} serves {restaurant.cuisine_type} food.')

restaurant.describe_restaurant()
restaurant.open_restaurant()
