# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-11
# --------------------------------------------------------------------------- #


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


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size."""
        print(f'This car has a {self.battery_size}-kilowatt-hour battery.')

    def get_range(self):
        """Print a statement bout the range the battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car,. specific to an electric car"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the paren class. Then initialize
        attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()


# my_new_car = Car('honda', 'ridgeline', '2019')
# print(f'\nMy new car is a {my_new_car.descriptive_name()}.')
# my_new_car.read_odometer()
# print()

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\nUpgrading battery...')
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
