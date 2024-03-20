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

    def encrypt_password(self):
        """
        Encrypt the user's password.
        :return: The encrypted password
        """
        return hashlib.sha256(self.password.encode()).hexdigest()
