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
