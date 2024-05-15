#!/usr/bin/python3
"""
User class
"""


class User():
    """ User class """

    def __init__(self):
        """ Init class User. """
        self.__email = None

    @property
    def email(self):
        """ User class getter """
        return self.__email

    @email.setter
    def email(self, value):
        """ User class settere """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

 
if __name__ == "__main__":
    """
    Main function to test User class.
    """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
