# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


class User:
    """User class"""

    def __init__(self, first_name, last_name, user_name, location):
        """Constructor for User"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.location = location.title()

    def describe_user(self):
        """Describe user."""
        print(f'\n{self.first_name} {self.last_name} (username: '
              f'{self.user_name}) lives in {self.location}.')

    def greet_user(self):
        """Greets user."""
        print(f'\nWelcome back, {self.first_name} {self.last_name}.')


user_1 = User('daniel', 'rodriguez', 'washirican', 'kirkland')
user_1.greet_user()
user_1.describe_user()

user_2 = User('natalia', 'gonzalez', 'natifutbolera', 'bogota')
user_2.greet_user()
user_2.describe_user()

user_3 = User('maicol', 'yoldan', 'la_cabra', 'chicago')
user_3.greet_user()
user_3.describe_user()

