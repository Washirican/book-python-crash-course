# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-13
# --------------------------------------------------------------------------- #


class User:
    """User class"""

    def __init__(self, first_name, last_name, user_name, location):
        """Constructor for User"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Describe user."""
        print(f'{self.first_name} {self.last_name} (username: '
              f'{self.user_name}) lives in {self.location}.')

    def greet_user(self):
        """Greets user."""
        print(f'Welcome back, {self.first_name} {self.last_name}.')

    def increment_login_attempts(self):
        """Increment login attempts by a given value."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts."""
        self.login_attempts = 0
