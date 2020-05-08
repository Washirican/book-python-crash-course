# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructor for Restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f'\n{self.restaurant_name} serves {self.cuisine_type} food.')

    def open_restaurant(self):
        """Open restaurant."""
        print(f'\n{self.restaurant_name} is now open!')


restaurant_1 = Restaurant('amaro bistro', 'italian')

# print(f'\n{restaurant_1.restaurant_name} serves {restaurant_1.cuisine_type} food.')

restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()


restaurant_2 = Restaurant('cactus', 'mexican')
restaurant_2.describe_restaurant()
# restaurant_2.open_restaurant()


restaurant_3 = Restaurant('isarn', 'thai')
restaurant_3.describe_restaurant()
# restaurant_3.open_restaurant()
