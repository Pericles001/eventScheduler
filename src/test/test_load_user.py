"""
File: test_load_user.py
Class: TestLoadUser - contains the tests for loading user data.
"""

import unittest

from src.io.user_save import SaveUser


class TestLoadUser(unittest.TestCase):
    """
    Class: TestLoadUser
    Purpose: contains the tests for loading user data.
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

    def test_load_user(self):
        """
        Test loading a user from the file
        :return:
        """
        users_data = self.save_user.load_users()
        print(users_data)
