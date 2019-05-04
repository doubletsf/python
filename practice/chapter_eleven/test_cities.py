import unittest
from city_function import city_country


class CityTestCase(unittest.TestCase):
    '''测试city_funtion.py'''

    def test_city_country(self):
        city_country_name = city_country('santiago', 'chile')
        self.assertEqual(city_country_name, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_name = city_country(
            'santiago', 'chile', '5000000')
        self.assertEqual(city_country_name,
                         'Santiago, Chile 5000000')


unittest.main()
