"""
File: test_user.py
Description: This file contains unit tests for the User class.
"""

import unittest

import python.src.model.user


class TestUser(unittest.TestCase):
    """
    Class: TestUser
    Purpose: contains the tests for the user object.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.user = python.src.model.user.User("username", "password", "email", "full_name", 1)

    def tearDown(self):
        """
        Tear down the test case.
        """
        del self.user

    def test_create_user(self):
        """
        Method: test_create_user
        Purpose: tests the create_user method.
        """
        self.assertEqual(self.user.username, "username")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.email, "email")
        self.assertEqual(self.user.full_name, "full_name")
