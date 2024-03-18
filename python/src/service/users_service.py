"""
File: users_service.py

This file defines the UsersService class, which provides methods for
managing users.
"""

import python.src.model.user as user
from python.src.repository.repository import UserRepository
from python.src.io.user_save import SaveUser


class UserService:
    """
    The UsersService class provides methods for managing users.
    """

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        """
        Create a new user.

        Args:
            user_data (dict): A dictionary containing the user's data.
        """
        user_username = user_data["username"]
        user_password = user_data["password"]
        user_email = user_data["email"]
        user_full_name = user_data["full_name"]
        user_status = user_data["status"]
        # Ensure correct order of arguments passed to the User constructor
        new_user = user.User(user_username, user_password, user_email, user_full_name, user_status)
        self.user_repository.add_user(new_user)
        details_saver = SaveUser()
        details_saver.save_user(new_user)

    def load_users(self):
        """
        Load the users from the file.
        """
        details_loader = SaveUser()
        details_loader.load_users()

    def get_user(self, username):
        """
        Get a user from the repository.

        Args:
            username (string): The name of the user to get.
        :returnurns:
            user.User: The user with the given username.
        """
        try:
            target_user = self.user_repository.get_user(username)
            return target_user
        except Exception as e:
            print("Error getting user:", e)
            return None

    def get_all_users(self):
        """
        Get all users from the repository.
        """
        return self.user_repository.get_all_users()

    def update_user(self, username, user_data):
        """
        Update a user in the repository.

        Args:
            username (string): The name of the user to update.
            user_data (dict): A dictionary containing the user's data.
        """

        user_username = user_data["username"]
        user_password = user_data["password"]
        user_email = user_data["email"]
        user_full_name = user_data["full_name"]
        user_status = user_data["status"]
        user_to_update = user.User(user_username, user_password, user_email, user_full_name, user_status)
        self.user_repository.update_user(username, user_to_update)

    def get_user_status(self, username):
        """
        Get the status of a user from the repository.
        :param username:
        :return:
        """
        target_user = self.user_repository.get_user(username)
        if target_user.status == 1:
            return "Active"
        else:
            return "Inactive"

    def save_user_details(self, user_data):
        """
        Save a user's details to the db file
        :param user_data: A dictionary containing user details.
        :return: True if the user details are saved successfully, False otherwise.
        """
        details_saver = SaveUser()
        username = user_data.get("username")  # Get the username from user_data
        target_user = self.user_repository.get_user(username)
        try:
            if target_user is not None:  # Check if target_user exists
                details_saver.save_user(target_user)
                print("User details saved successfully!")
                return True
            else:
                print("Error: User not found.")
                return False
        except Exception as e:
            print("Error saving user details:", e)
            return False

    def delete_user(self, username):
        """
        Delete a user from the repository.
        :param username:
        :return:
        """
        self.user_repository.delete_user(username)

    # def login_user(self, user_data):
    #     """
    #     Log in a user.
    #     Use the user function login from class User
    #     :param user_data:
    #     :return:
    #     """
    #     username = user_data["username"]
    #     password = user_data["password"]
    #     target_user = SaveUser.get_user(username)
    #     print(target_user)

    # def login_user(self, user_data):
    #     """
    #     Log in a user.
    #     Use the user function login from class User
    #     :param user_data:
    #     :return:
    #     """
    #     username = user_data["username"]
    #     password = user_data["password"]
    #     # Fetch the user from the repository using UserService
    #     target_user = SaveUser.get_user(username)
    #     print(target_user)

    def login_user(self, user_data):
        """
        Log in a user.

        Args:
            user_data (dict): A dictionary containing the user's data.
        """
        username = user_data["username"]
        password = user_data["password"]
        # Fetch the user from the repository using UserService
        target_user = self.get_user(username)  # Use the UserService method to get the user
        if target_user is not None:
            if target_user.password == password:  # Check if passwords match
                print("User logged in successfully!")
                return target_user  # Return the logged-in user
            else:
                print("Invalid password!")
                return None
        else:
            print("User not found!")
            return None

    def logout_user(self, username):
        """
        Log out a user.
        Use the user function logout from class User
        :param username:
        :return:
        """
        target_user = self.user_repository.get_user(username)
        if target_user is not None:
            target_user.logout()
            SaveUser.update_user_details(target_user)
            print("User logged out successfully!")
        else:
            print("User not found!")
