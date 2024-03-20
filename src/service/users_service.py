"""
File: users_service.py

This file defines the UsersService class, which provides methods for
managing users.
"""
import hashlib
import json

import src.model.user as user
import src.utils.utils as utils
from src.io.user_save import SaveUser, load_users
from src.repository.repository import UserRepository

daily_logger = utils.create_log_file_if_not_exists()


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
        try:
            user_username = user_data["username"]
            user_password = user_data["password"]
            user_email = user_data["email"]
            user_full_name = user_data["full_name"]
            user_status = user_data["status"]
            user_events = user_data["events"]
            new_user = user.User(user_username, user_password, user_email, user_full_name, user_status, user_events)
            # Create an instance of SaveUser
            user_saver = SaveUser()
            # Call save_user method on the instance
            user_saver.save_user(new_user)
            print("User created successfully!")
        except Exception as e:
            print("Error creating user:", e)

    def load_users(self):
        """
        Load the users from the file.
        """
        details_loader = SaveUser()
        try:
            users = details_loader.load_users()
            return users
        except Exception as e:
            print("Error loading user details:", e)
            return {}

    def get_user(self, old_users, username):
        """
        Get a user from the file database.
        :param old_users: Dictionary containing user data.
        :param username: Username of the user to get.
        :return: User object if found, None otherwise.
        """
        if username in old_users:
            user_data = old_users[username]
            return user.User(user_data["username"], user_data["password"], user_data["email"],
                             user_data["full_name"], user_data["status"], user_data["events"])
        else:
            return None

    def get_all_users(self):
        """
        Get all users from the repository.
        """
        return self.user_repository.get_all_users()

    def update_user(self, username, user_data, sys_users, datafile_path):
        """
        Update a user in the repository.

        Args:
            username (string): The name of the user to update.
            user_data (dict): A dictionary containing the user's data.
        """
        try:
            if username in sys_users:
                sys_users[username] = user_data
                with open(datafile_path, "w") as f:
                    json.dump(list(sys_users.values()), f, indent=4)
                print("User updated successfully!")
            #     return the updated user
            else:
                print("User not found!")
        except Exception as e:
            print("Error updating user details:", e)

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

    @staticmethod
    def update_user_details(user_data):
        """Update user details in the users.json file.

        Args:
            user_data (list): List of dictionaries containing user data.

        Returns:
            None
        """
        return

    def update_user_status(self, users, username, user_data):
        """
        Update a user in the file database
        :param users:
        :param username:
        :param user_data:
        :return:
        """
        # Create a new list to store the updated user data
        updated_users = []
        # Iterate through the users
        for user in users:
            # Check if the user is the one to be updated
            if user["username"] == username:
                # Update the user data
                user.update(user_data)
            # Add the user to the updated list
            updated_users.append(user)
        # Write the updated user data to the file
        with open("data/out/users.json", "w") as f:
            json.dump(updated_users, f, indent=4)

    def login_user(self, user_data):
        """
        Log in a user.

        Args:
            user_data (dict): A dictionary containing the user's data.

        Returns:
            User: The logged-in user object if successful, None otherwise.
        """
        username = user_data["username"]
        password = user_data["password"]

        # Load user data from file
        users_data = load_users()
        # Check if user exists
        if username in users_data:
            target_user = users_data[username]
            stored_password = target_user["password"]
            # Encrypt the entered password
            encrypted_password = hashlib.sha256(password.encode()).hexdigest()

            if stored_password == encrypted_password:
                # Update user status to online (status = 1)
                target_user["status"] = 1

                # Update user data in file
                with open("data/out/users.json", "w") as f:
                    json.dump(list(users_data.values()), f, indent=4)

                print("User logged in successfully!")
                return user.User(target_user["username"], target_user["password"], target_user["email"],
                                 target_user["full_name"], target_user["status"], target_user["events"])
            else:
                print("Invalid password!")
                return None
        else:
            print("User not found!")
            return None

    def logout_user(self, old_users, username):
        """
        Log out a user.
        :param old_users: Dictionary containing user data.
        :param username: Username of the user to log out.
        :return: Message indicating whether the user was successfully logged out or not.
        """
        if username in old_users:
            # Set the user's status to offline (status = 0)
            print("Logging out user: ", username)  # Debugging line to check username
            old_users[username]["status"] = 0

            # Write the updated user data back to the file
            file_path = "data/out/users.json"
            try:
                with open(file_path, "w") as f:
                    old_users_list = []
                    for key, value in old_users.items():
                        old_users_list.append(value)
                    json.dump(old_users_list, f, indent=4)
                return "User logged out successfully!"
            except Exception as e:
                return f"Error updating user details: {e}"
        else:
            return "User not found!"

    def get_user_details(self, username, sys_users):
        """
        Get user details from the users database.
        :param username:
        :param sys_users:
        :return:
        """
        try:
            if username in sys_users:
                user_details = sys_users[username]
                print(
                    f"Username: {user_details['username']}\nEmail: {user_details['email']}\n"
                    f"Full Name: {user_details['full_name']}\nStatus: {user_details['status']}"
                    f"\nEvents: {user_details['events']}")
            else:
                print("User not found!")
        except Exception as e:
            print(f"Error getting user details: {e}")
        return None

    def delete_user(self, username, sys_users, datafile):
        """
        Delete a user from the file database.
        :param username:
        :param sys_users:
        :param datafile:
        :return:
        """
        try:
            if username in sys_users:
                del sys_users[username]
                with open(datafile, "w") as f:
                    json.dump(list(sys_users.values()), f, indent=4)
                print("User deleted successfully!")
            else:
                print("User not found!")
        except Exception as e:
            print("Error deleting user:", e)
