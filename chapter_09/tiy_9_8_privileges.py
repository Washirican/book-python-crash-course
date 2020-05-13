# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-11
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


class Admin(User):
    """Admin class"""

    def __init__(self, first_name, last_name, user_name, location):
        """Constructor for Admin"""
        super().__init__(first_name, last_name, user_name, location)
        self.privileges = Privileges()


class Privileges:
    """Privileges class"""

    def __init__(self, privileges=[]):
        """Constructor for Privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Show admin privileges."""
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print('This user has no admin privileges.')


# user_1 = User('james', 'rodriguez', 'el_gago', 'madrid')
# user_1.greet_user()
# user_1.describe_user()

admin = Admin('daniel', 'rodriguez', 'washirican', 'kirkland')
# admin.greet_user()
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")
admin.privileges.privileges = ['can add post', 'can delete post', 'can ban user']

admin.privileges.show_privileges()
