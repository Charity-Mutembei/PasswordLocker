from User import User

#we are now creating functions to implement the tests tested
#test one- create a user account

def create_userAccount(fname, lname, username, phoneNumber, email):
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
def find_contact(number, user_name):
    '''
    Function to find a user by number or username and returns the user information
    '''
    return User.find_by_number(number)
    return User.find_by_username (user_name)

#test five- check if the user exists function
def check_existing_users(number, email):
    '''
    Function that check ig a user does exist with that number and return a Boolean
    '''
    return User.user_exists(number)
    return User.user_exists(email)

#test six- check if all the user accounts accounts by displaying them
def display_users():
    '''
    Function that returns all the saved user accounts/information
    '''
    return User.display_users()
