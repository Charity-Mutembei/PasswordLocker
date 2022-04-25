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

