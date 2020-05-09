# class Car:
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Constructor for Car"""
        self.make = make
        self.model = model
        self.year = year

        # Define attribute with default value
        self.odometer_reading = 0

    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Prints odometer reading."""
        print(f'This car has {self.odometer_reading} miles on it.')

    # Use class method to update attribute
    def update_odometer(self, mileage):
        """
        Updates odometer reading to a give value. Reject change is
        someone tries to roll back the odometer reading.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('\nYou can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        """Increment odometer by a given value."""

        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('\nYou can\'t give negative miles to roll back an odometer!')


my_old_car = Car('nissan', 'frontier', '2015')
print(f'\nMy old car was a {my_old_car.descriptive_name()}.')
my_old_car.read_odometer()

my_new_car = Car('honda', 'ridgeline', '2019')
print(f'\nMy new car is a {my_new_car.descriptive_name()}.')
my_new_car.read_odometer()

# Update instance attributes directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
