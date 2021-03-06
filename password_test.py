import unittest
import pyperclip
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
    
    def test_find_user_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User('Test', 'user', 'user_name', '0702659321', 'test@user.com')
        test_user.save_user()
        found_user = User.find_by_number ('0702659321')
        self.assertEqual(found_user.email, test_user.email)
        
    
    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we can find/cannot find the user
        '''

        self.new_user.save_user()
        test_user = User ('Test', 'user', 'user_name', '0702659321', 'test@user.com')
        test_user.save_user()

        user_exists = User.user_exists('0702659321')
        self.assertTrue(user_exists)

        #this method demands for a class method as well
    
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(), User.user_list)

        #this requires a classmethod
    
    # def test_copy_email(self):
    #     '''
    #     test to confirm that we are copying the email address from a found user
    #     '''

    #     self.new_user.save_user()
    #     User.copy_email('0702659321')

    #     self.assertEqual(self.new_user.email, pyperclip.paste ())

    #     #this needs a classmethod as well



if __name__ == '__main__':
    unittest.main()