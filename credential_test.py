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
        self.new_credentials = Credentials('Charity', 'Mutembei', 'Cherry', '0721263471', 'charry@gmail.com', 'password')

    def tearDown(self):
        '''
        tearDown Method that des clean up after each test case has run
        '''
        Credentials.password_list = []

    def test_init (self):
        '''
        test_init test case to test if the objects is initialised properly
        '''
        self.assertEqual(self.new_credentials.first_name, 'James')
        self.assertEqual(self.new_credentials.last_name, 'Muriuki')
        self.assertEqual(self.new_credentials.user_name, 'Cherry')
        self.assertEqual(self.new_credentials.phone_number, '0712345678')
        self.assertEqual(self.new_credentials.email, 'james@ms.com')
        self.assertEqual(self.new_credentials.password, '23232323')
    
    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.password_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact objects to our contact_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Test', 'user', '0711223344', 'test@user.com')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.password_list), 2)
    
    def test_find_credentials_by_number(self):
        '''
        test to check if we find a contact by phone number and display information
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials ('Test', 'user', '0702659321', 'test@user.com')
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_number ('0711223344')

        self.assertEqual(found_credentials.email,test_credentials.email)
    
    def test_credentials_exists(self): #here we created a test case called contact_exists method
        '''
        test to check if we can return a boolean if we cannot find the contact
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Test', 'user', '0702659321', 'test@user.com')
        test_credentials.save_credentials()
        credentials_exists = Credentials.credentials_exists('0702659321') #which takes a phone number
        self.assertTrue(credentials_exists)    #we use the assertTrue method to check if the number is there to return True(Boolean)


    def test_display_all_credentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.password_list)  

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found contact
    #     '''

    #     self.new_contact.save_contact()
    #     Contact.copy_email('0712345678')

    #     self.assertEqual(self.new_contact.email, pyperclip.paste())
  

   


if __name__ == '__main__':
    unittest.main()
