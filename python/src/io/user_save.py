"""
File: user_save.py
Class: SaveUser - contains the methods for saving and retrieving user data.

"""
import os


def load_users():
    """
    Load the users from the file.

    Returns:
        None
    """
    users = {}
    try:
        file_path = "data/out/users.txt"
        with open(file_path, "r") as in_file:
            # Check if the file is empty
            if os.stat(file_path).st_size == 0:
                print("User details file is empty.")
                return

            user_id = 0  # Unique identifier for each user
            for line in in_file:
                user_data = line.strip().split(",")  # Strip to remove trailing newline
                # Check if the user data is not empty
                if user_data:
                    # Save all the user data in a dictionary with unique identifier as key
                    users[user_id] = user_data
                    user_id += 1  # Increment the unique identifier for the next user
        print("User details loaded successfully!")
    except Exception as e:
        print("Error loading user details:", e)
    finally:
        in_file.close()
        return users


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
        file_path = "data/out/users.txt"
        try:
            # Check if the directory exists, create it if not
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Write user information to the file
            with open(file_path, "a") as out_file:
                out_file.write(user.username + "," + user.encrypt_password() + "," + user.email + ","
                               + user.full_name + "," + str(user.status) + "\n")
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

    def update_user_details(self, user):
        """
        Update a user's details in the file.
        :param user:
        :return:
        """
        in_file = open("../../data/out/users.txt", "r")
        out_file = open("../../data/out/users.txt", "w")
        for line in in_file:
            user_data = line.split(",")
            if user_data[0] == user.username:
                out_file.write(
                    user.username + "," + user.encrypt_password() + "," + user.email + "," + user.full_name + ","
                    + user.status + "\n")
            else:
                out_file.write(line)
        in_file.close()
        out_file.close()

    def load_users(self):
        return load_users()
