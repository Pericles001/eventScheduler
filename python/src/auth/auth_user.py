"""
File: auth_user.py
Purpose: contains the user object and the user service.
"""

import hashlib


class AuthUser:
    """
    Class: AuthUser
    Purpose: class used to check user authentication
    """

    def __init__(self, username, password):
        """
        Initialize a new user.
        :param username: The user's username.
        :param password: The user's password.
        """
        self.username = username
        self.password = password

    def authenticate(self):
        """
        Authenticate the user.
        :return: True if the user is authenticated, False otherwise
        """
        users_file = open("../../data/out/users.txt", "r")
        for line in users_file:
            user_data = line.split(",")
            if user_data[0] == self.username:
                if user_data[1] == self.encrypt_password():
                    return True
        return False

    def check_status(self):
        """
        Check the status of the user.
        :return: The status of the user
        """
        users_file = open("../../data/out/users.txt", "r")
        for line in users_file:
            user_data = line.split(",")
            if user_data[0] == self.username:
                return user_data[4]
        return None

    def encrypt_password(self):
        """
        Encrypt the user's password.
        :return: The encrypted password
        """
        return hashlib.sha256(self.password.encode()).hexdigest()
