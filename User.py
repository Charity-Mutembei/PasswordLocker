import re
import pyperclip


class User:
    '''
    Class that generates new instances of the Users
    '''
    pass

    user_list = []


    def __init__(self, first_name, last_name, user_name,phone_number, email):
        '''
        The properties needed by the application for the user will require, their names, 
        their usernames, phone numbers and emails

        Args: 
        first_name: new user first name.
        last_name: new user first name.
        user_name: new user user name.
        phone_number: new user phone number.
        email: new contact email address. 
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
    def save_user(self):
        '''
        save_user method saves users as objects into the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    
    @classmethod
    def find_by_username(cls,user_name):
        '''
        Method that takes in a username and returns a user that matches the username
        
        Args:
         username: user_name to search for
        Returns:
        user account of the person that matches the username.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user  
    
    #this class method is a decorator
    
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a number and returns a conatct that matches the number 

        Args: 
        number: phone number to search for 
        Returns:
        User that the phone number matches with
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return user


    @classmethod
    def user_exists (cls, number):
        '''
        Method that checks if a user exists from the user list

        Args: 
        number: phone number to search if it exists
        Returns:
        Boolean: True or False depending if the contact exists 
        '''
        
        for user in cls.user_list:
            if user.phone_number == number:
                return True 
            
        return False
    
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
    # @classmethod

    # def copy_email(cls, number):
    #     user_found = User.find_by_number(number)
    #     pyperclip.copy(user_found.email)

class Credentials:
    '''
    class the generates passwords for the user
    '''
    pass 

    password_list = []

    def __init__(self, first_name, last_name, user_name, phone_number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.email= email
        self.password = password
    def save_credentials(self):
        '''
        save_password method that saves the password object of each user into the password_list
        '''
        Credentials.password_list.append(self)
    @classmethod
    def find_by_number (cls, number):
        '''
        method that takes in numbers and returns a contact that match 
        Args:
        number: phone number to search for
        Returns: 
        user credentials that matches the number
        '''
        for credentials in cls.password_list:
            if credentials.phone_number == number:
                return credentials
        
        @classmethod
        def credentials_exists(cls, number):
            '''
            method that checks if the credentials exists from the password lists 
            Args:
            number: phone number to search if it exists
            Returns:
            Boolean: true or false depending if the credentials exists
            '''
            for credentials in cls.password_list:
                if credentials.phone_number == number:
                    return True
            
            return False

        @classmethod
        def display_credentials (cls):
            '''
            method that returns the password list
            '''
            return cls.password_list

            # @classmethod
            # def copy_email (cls, number):
            #     credentials_found = Credentials.find_by_number(number)
            #     pyperclip


    



