import unittest
from User import User

class TestUser(unittest.TestCase):

    '''
    Test class that defies test cases for the user class behaviors
    Args: 
    unittest.TestCase: TestCase Class that helps in creating test cases
    '''

        #test1-input user
    def setUp(self):
        '''
        to be run before each class
        '''
        self.new_user = User('Charity', 'Mutembei', 'Cherry', '0721263471', 'charry@gmail.com')

    def tearDown(self):
        '''
        tearDown method that clea up after each test
        '''

        User.user_list = []

    def test_init (self):
        '''
        test if there is proper initialization of the objects
        '''

        self.assertEqual(self.new_user.first_name, 'Charity')
        self.assertEqual(self.new_user.last_name, 'Mutembei')
        self.assertEqual(self.new_user.user_name, 'Cherry')
        self.assertEqual (self.new_user.phone_number, '0721263471')
        self.assertEqual(self.new_user.email, 'charry@gmail.com')

    #test2-save user

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        #this needs a link to the class file as a method to make the test pass. 

    #test3- save multiple users 

    def test_save_multiple_user(self):
        '''
        test_save_multiple_users to cehck if we can have more than one user in the user list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'user', 'username', '0702659321', 'test@user.com') #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from out user list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'user', 'username', '0702659321', 'test@user.com')
        test_user.save_user()

        self.new_user.delete_user()

        self.assertEqual(len(User.user_list),1)

        #we added the above method to the class as well. 
        #test-5 - findinf a user by username
    def test_find_user_by_username(self):
        '''
        test to check if we can find a contact by username and display information
        '''

        self.new_user.save_user()
        test_user = User('Test', 'user', 'user_name', '0702659321', 'test@user.com')
        test_user.save_user()

        found_user = User.find_by_username('user_name')
        self.assertEqual(found_user.email, test_user.email)

        #the above method requires a class method in the user document/file


if __name__ == '__main__':
    unittest.main()