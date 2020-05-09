# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-08
# --------------------------------------------------------------------------- #


class Restaurant:
    """Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructor for Restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f'{self.restaurant_name} serves {self.cuisine_type} food.')

    def open_restaurant(self):
        """Open restaurant."""
        print(f'{self.restaurant_name} is now open!')

    def set_number_served(self, customers_served):
        """Set number served to a given value."""
        self.number_served = customers_served

    def increment_number_served(self, new_served):
        """Increments number served by given value."""
        if new_served >= 0:
            self.number_served += new_served
        else:
            print('Can\'t decrease number served!')


restaurant = Restaurant('amaro bistro', 'italian')

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

print('\n------------------------------------')
# Change instance attribute directly
restaurant.number_served = 10
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

print('\n------------------------------------')
# Create class method to change attribute
restaurant.set_number_served(12)
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

print('\n------------------------------------')
# Create class method to increment attribute
restaurant.increment_number_served(100)
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

