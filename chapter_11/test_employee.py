# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-28
# --------------------------------------------------------------------------- #

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for Employee class."""

    def setUp(self):
        """Create a base employee to use in all test cases."""
        self.employee = Employee('Daniel', 'Rodriguez', 120_000)

    def test_default_salary_increase(self):
        """Test default salary increase of $5,000."""
        self.employee.give_rise()
        self.assertEqual(self.employee.salary, 125_000)

    def test_salary_increase(self):
        """Test salary increase by any amount."""
        self.employee.give_rise(15_000)
        self.assertEqual(self.employee.salary, 135_000)


if __name__ == '__main__':
    unittest.main()
