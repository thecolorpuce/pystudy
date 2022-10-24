import unittest
import city_functions as fc

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""
    
    def test_city_country(self):
        """Do names like 'minneapolis, united states' work?"""
        formatted_name = fc.formatted_city('minneapolis', 'united states')
        self.assertEqual(formatted_name, 'Minneapolis, United States')
    
    def test_city_country_pop(self):
        """Testing population"""
        formatted_name = fc.formatted_city_population('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile | Population: 5000000')

if __name__ == '__main__':
    unittest.main()