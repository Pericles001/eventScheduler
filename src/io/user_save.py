"""
File: user_save.py
Class: SaveUser - contains the methods for saving and retrieving user data.

"""
import json
import os

import src.utils.utils as utils


def load_users():
    """
    Load the users from the users.json file.

    Returns:
        dict: A dictionary containing user data.
    """
    users = {}
    file_path = "data/out/users.json"
    log_file = utils.create_log_file_if_not_exists()
    try:
        with open(file_path, "r") as f:
            if os.stat(file_path).st_size == 0:
                return {}
            users_data = json.load(f)
            if isinstance(users_data, list):
                for user_data in users_data:
                    username = user_data["username"]
                    users[username] = user_data
            elif isinstance(users_data, dict):
                # convert the dictionary to a list of dictionaries
                users = users_data
                for user in users:
                    users[user] = users_data[user]
            else:
                print("Unexpected format in users.json:", type(users_data))
        utils.write_to_daily_log_file("User details loaded successfully!" + "\n", log_file)
        return users
    except FileNotFoundError:
        print("User details file not found.")
        return {}
    except Exception as e:
        print("Error loading user details:", e)
        return {}


class SaveUser:
    """
    Class: SaveUser
    Purpose: contains the methods for saving and retrieving user data.
    """

    def __init__(self):
        """
        Initialize the SaveUser class.
        """
        self.users = {}

    def save_user(self, user):
        """
        Save a user informations in a file.

        Args:
            user (User): The user to save.

        Returns:
            None
        """
        file_path = "data/out/users.json"
        try:
            # Check if the directory exists, create it if not
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Load existing user data
            if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
                with open(file_path, "r") as f:
                    users_data = json.load(f)
            else:
                users_data = []

            # Convert user object to dictionary
            user_dict = {
                "username": user.username,
                "password": user.encrypt_password(),
                "email": user.email,
                "full_name": user.full_name,
                "status": user.status,
                "events": [{"title": event.title, "date": event.date, "description": event.description}
                           for event in user.events]
            }

            # Append user data to existing data
            users_data.append(user_dict)

            # Write user information to the file
            with open(file_path, "w") as f:
                json.dump(users_data, f, indent=4)

            print("User details saved successfully!")
        except Exception as e:
            print("Error saving user details:", e)

    def get_user(self, username):
        """
        Get a user informations from the file.
        :param username:
        :return:
        """
        in_file = open("data/out/users.txt", "r")
        for line in in_file:
            user_data = line.split(",")
            if user_data[0] == username:
                return user_data
        return None

    @staticmethod
    def update_user_details(user_data):
        """
        Update user details in the users.json file.

        Args:
            user_data (dict): Dictionary containing user data.

        Returns:
            None
        """
        file_path = "data/out/users.json"
        try:
            # Open the users.json file for reading
            with open(file_path, "r") as file:
                existing_data = json.load(file)

            # Update existing user data or append new user data
            updated_data = existing_data.copy()
            for user in user_data:
                username = user["username"]
                # Find the index of the user in the existing data
                user_index = next((index for index, u in enumerate(updated_data) if u["username"] == username), None)
                if user_index is not None:
                    # Update user data if found
                    updated_data[user_index] = user
                else:
                    # Append user data if not found
                    updated_data.append(user)

            # Write the updated user data to the file
            with open(file_path, "w") as file:
                json.dump(updated_data, file, indent=4)

            print("User details updated successfully!")
        except Exception as e:
            print("Error updating user details:", e)

    def load_users(self):
        return load_users()
