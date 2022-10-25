import unittest
import oneonethree as oot

class TestEmployee(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        self.employee = oot.Employee('riley', 'abbs', 5000)
        self.testraise = 10000
        
    def test_given_default_raise(self):
        """Test the default raise of 5000"""
        self.employee.give_raise()
        default_raise = self.employee.name_employee()
        self.assertEqual(self.employee.name_employee(), 'Riley, Abbs 10000')
    
    def test_give_custom_raise(self):
        """Test a custom raise"""
        custom_raise = self.employee.give_raise(self.testraise)
        self.assertEqual(self.employee.name_employee(), 'Riley, Abbs 15000')

if __name__ == '__main__':
    unittest.main()