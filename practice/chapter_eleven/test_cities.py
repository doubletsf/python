import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase):
    '''测试city_funtion.py'''

    def test_city_country(self):
        '''能够正确处理santiago, chile这样的名字吗 '''
        city_country_name  = city_country('santiago', 'chile')
        self.assertEqual(city_country_name , 'Santiago, Chile')

unittest.main()

