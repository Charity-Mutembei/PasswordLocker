from typing import Tuple
from User import User

#we are now creating functions to implement the tests tested
#test one- create a user account

def create_user(fname, lname, username, phoneNumber, email):
    '''
    Function that allows a user create an account
    '''
    new_user = User(fname, lname, username, phoneNumber, email)
    return new_user

#test two- create a saves users/accounts info function
def save_users(user):
    '''
    Function to save the users
    '''
    user.save_user()

#test three- delete user functions 
def del_user(user):
    '''
    Function to delete user
    '''
    user .delete_user()

#test four- finding the user functions 
def find_user(phone_number, user_name):
    '''
    Function to find a user by number or username and returns the user information
    '''
    return User.find_by_number(phone_number)
    return User.find_by_username (user_name)

#test five- check if the user exists function
def check_existing_users(phone_number, email):
    '''
    Function that check ig a user does exist with that number and return a Boolean
    '''
    return User.user_exists(phone_number)
    return User.user_exists(email)

#test six- check if all the user accounts accounts by displaying them
def display_users():
    '''
    Function that returns all the saved user accounts/information
    '''
    return User.display_users()

#below is the main function
def main():
    print ('Hello, Welcome to the Password Locker. What is your name?')
    user_name = input()
    print (f'Hello {user_name}. How can we help you today?')

    print ('\n')
    while True:
        print ('use this short codes to commence: cc - Creates a new account in the passwordLocker, lc- logs you in into an already existing account in the passwordLocker, vc- allows you to see the list of accounts and their passwords present in the passwordLocker, dc- allows you to delete accounts you perhaps do not want anymore, ex-exit')
        short_code = input().lower()
        if short_code == 'cc':
            print ('New Contact')
            print ('_'*10)

            print ('First Name')
            f_name = input()

            print ('Last Name')
            l_name = input ()

            print ('User Name of choice')
            u_name = input ()

            print ('Phone Number')
            p_number = input()

            print ('email address')
            e_address = input()

            save_users(create_user (f_name, l_name, u_name, p_number, e_address))

            print('\n')
            print (f'new User {u_name} created')
            print('\n')

        # elif short_code == 'lc':
        #     if log_in():
        #         print ('User Name')
        #         u_name = input()
        #         print ('Password')
        #         pName = input ()
        
        elif short_code == 'vc':
            if display_users():
                print ('Here is a list of all accouts registered')
                print('\n')
                for user in display_users():
                    print (f'{user.first_name} {user.last_name} {user.username} {user.phone_number} {user.email}')
                    print ('\n')
        
        elif short_code == 'dc':
            if del_user(user):
                print ('Enter user name of the account you wish to delete')
                user_name = input()
                print ('Enter the phone number used to register the account')
                phone_number = input()

                print ('\n')

                print ('{user.user_name} {user.number} .....Y/n')


                del_user(find_user(phone_number, user_name))
                print ('{user.user_name} deleted')
            
        elif short_code == 'ex':
            print('Have a lovely day ahead')
        else:
            print ('Command not found. Consider restarting and using the provided shortcodes')
        

if __name__ == '__main__':
    main()
            

