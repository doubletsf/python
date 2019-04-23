'''
    要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个
继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试.
'''
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确地处理像Janis Joplin这样的名字吗？'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        '''能够正确处理wolfgang Amadeus Mozart这样的名字吗'''
        formaaated_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formaaated_name, 'Wolfgang Amadeus Mozart')
unittest.main()