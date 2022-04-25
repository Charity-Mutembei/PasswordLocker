from User import Credentials
import unittest
class TestContact (unittest.TestCase):
    '''
    Test class that defines test cases for the user accounts class behavior 
    Args: 
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test case. 
        '''
        self.new_credentials = Credentials('Charity', 'Mutembei', 'Cherry', '0721263471', 'charry@gmail.com')

    def tearDown(self):
        '''
        tearDown Method that des clean up after each test case has run
        '''
        Credentials.password_list = []

    