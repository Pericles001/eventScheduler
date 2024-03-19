"""
File: user.py
Class: User - contains the user object
"""
import hashlib
import python.src.auth.auth_user as auth_user


class User:
    """
    Class: User
    Purpose: represents the user object of the system
    """

    def __init__(self, username, password, email, full_name, status, events=None):
        """
        Initialize a new user.

        Args:
            username (str): The user's username.
            password (str): The user's password.
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            events (list): The user's events.
        """
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name
        self.status = status
        self.events = events

    # Getters and setters for the user's attributes

    @property
    def username(self):
        """
        Get/set the username of the user
        :return: current username
        """
        return self.__username

    @username.setter
    def username(self, value):
        """
        Set the username of the user
        :param value: the new username
        """
        self.__username = value

    @property
    def password(self):
        """
        Get/set the password of the user
        :return: current password
        """
        return self.__password

    @password.setter
    def password(self, value):
        """
        Set the password of the user
        :param value: the new password
        """
        self.__password = value

    @property
    def email(self):
        """
        Get/set the email of the user
        :return: current email
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Set the email of the user
        :param value: the new email
        """
        self.__email = value

    @property
    def full_name(self):
        """
        Get/set the full name of the user
        :return: current full name
        """
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        """
        Set the full name of the user
        :param value: the new first name
        """
        self.__full_name = value

    @property
    def status(self):
        """
        Get/set the status of the user
        :return: current status
        """
        return self.__status

    @status.setter
    def status(self, value):
        """
        Set the status of the user
        :param value: the new status
        """
        self.__status = value


    @property
    def events(self):
        """
        Get/set the events of the user
        :return: current events
        """
        return self.__events

    @events.setter
    def events(self, value):
        """
        Set the events of the user
        :param value: the new events
        """
        self.__events = value

    def print_user(self):
        """
        Print the user's information
        """
        print(
            "Username: " + self.username + "\nPassword: " + self.password + "\nEmail: " + self.email + "\nFull Name: "
            + self.full_name + "\nStatus: " + str(self.status) + "\nEvents: " + str(self.events) + "\n"
        )

    # Magic methods

    def __str__(self):
        """
        Method: __str__
        :return:
        """
        return f"Username: {self.__username} | Email: {self.__email} | Full Name: {self.__full_name}"

    def encrypt_password(self):
        """
        Encrypt the user's password using the SHA256 algorithm.
        """
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return self.password

    def decrypt_password(self):
        """
        Decrypt the user's password using the SHA256 algorithm.
        """
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return self.password

    # def login(self):
    #     """
    #     Login the user.
    #     :return: True if the user is authenticated, False otherwise, using the AuthUser class
    #     """
    #     user_auth = auth_user.AuthUser(self.username, self.password)
    #     authenticated = user_auth.authenticate()
    #     if authenticated:
    #         self.status = 1
    #     else:
    #         self.status = 0
    #     return authenticated

    def logout(self):
        """
        Logout the user
        Use the AuthUser class
        """
        user = auth_user.AuthUser(self.username, self.password)
        user.check_status()

        if user.status == 1:
            self.status = 0
        else:
            self.status = 0
