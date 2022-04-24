import unittest
from User import User

class TestUser(unittest.TestCase):

    '''
    Test class that defies test cases for the user class behaviors
    Args: 
    unittest.TestCase: TestCase Class that helps in creating test cases
    '''

    #test1
def setUp(self):
    '''
    to be run before each class
    '''
    self.new_user = User('Charity', 'Mutembei', 'Cherry', '0721263471', 'charry@gmail.com')

def test_init (self):
    '''
    test if there is proper initialization of the objects
    '''

    self.assertEqual(self.new_user.first_name, 'Charity')
    self.asertEqual(self.new_user.last_name, 'Mutembei')
    self.assertEqual(self.new_user.user_name, 'Cherry')
    self.assertEqual (self.new_user.phone_number, '0721263471')
    self.assertEqual(self.new_user.email, 'charry@gmail.com')

if __name__ == '__main__':
    unittest.main()