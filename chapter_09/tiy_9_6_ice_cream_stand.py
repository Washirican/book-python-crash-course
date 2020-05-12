# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-11
# --------------------------------------------------------------------------- #


class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructor for Restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f'\n{self.restaurant_name} serves {self.cuisine_type}.')

    def open_restaurant(self):
        """Open restaurant."""
        print(f'\n{self.restaurant_name} is now open!')


class IceCreamStand(Restaurant):
    """
    A simple Ice Cream Stand class that inherits from the Restaurant class
    """

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Constructor for IceCreamStand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Print a statement describing available ice cream flavors."""
        print(f'Available flavors are: ')
        for flavor in self.flavors:
            print(f'\t{flavor.title()}')


# Creating instance
ice_cream_shop = IceCreamStand('la tuya por si acaso')
# Initializing flavors instance attribute
ice_cream_shop.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio']

ice_cream_shop.describe_restaurant()
ice_cream_shop.show_flavors()
