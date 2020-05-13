# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
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
