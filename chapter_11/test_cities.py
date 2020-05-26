import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Test that city, country and population are formatted correctly."""
    def test_city_country_population(self):
        formatted_string = city_country('bogota', 'colombia', '10,779,000')
        self.assertEqual(formatted_string, 'Bogota, Colombia - '
                                           'population 10,779,000')

    def test_city_country(self):
        """Test that city, country is formatted correctly."""
        formatted_string = city_country('bogota', 'colombia')
        self.assertEqual(formatted_string, 'Bogota, Colombia')


if __name__ == '__main__':
    unittest.main()
