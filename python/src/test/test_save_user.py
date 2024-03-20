"""
File: test_save_user.py
Class: TestSaveUser - contains the tests for saving and retrieving user data.
"""

import unittest

from python.src.io.user_save import SaveUser
from python.src.model.user import User


class TestSaveUser(unittest.TestCase):
    """
    Class: TestSaveUser
    Purpose: contains the tests for saving and retrieving user data.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.save_user = SaveUser()

    def tearDown(self):
        """
        Tear down the test case.
        """
        pass

    def test_save_user(self):
        """
        Test saving a user to the file
        :return:
        """
        user = {
            "username": "test_username",
            "password": "test_password",
            "email": "test_email",
            "full_name": "test_full_name",
            "status": 0
        }

        new_user = User(user["username"], user["password"], user["email"], user["full_name"], user["status"])
        self.save_user.save_user(new_user)
        user_data = self.save_user.get_user("test_username")
        self.assertEqual(user_data[0], "test_username")
        self.assertEqual(user_data[1], "test_password")
        self.assertEqual(user_data[2], "test_email")
