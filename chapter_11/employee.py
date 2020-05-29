# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-28
# --------------------------------------------------------------------------- #


class Employee:
    """Basic employee class."""

    def __init__(self, first_name, last_name, salary):
        """Constructor for Employee"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_rise(self, salary_increase=5_000):
        """Give salary rise."""
        self.salary += salary_increase

