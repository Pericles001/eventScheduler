"""
File: test_user_service.py
Description: Test the user service.
"""

import unittest
import python.src.model.user
import python.src.service.users_service as services
import python.src.repository.repository as repo


class TestUserService(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case.
        """
        self.user_service = services.UserService()
        self.user = python.src.model.user

    def tearDown(self):
        """
        Tear down the test case.
        """
        pass

    def test_create_user(self):
        """
        Test the create_user method.

        :return:
        """
        user_data = {

            "username": "test_username",
            "password": "test_password",
            "email": "test_email",
            "full_name": "test_full_name",
            "status": 0
        }
        self.user_service.create_user(user_data)
        self.assertEqual(self.user_service.get_user("test_username").username, "test_username")
        self.assertEqual(self.user_service.get_user("test_username").password, "test_password")
        self.assertEqual(self.user_service.get_user("test_username").email, "test_email")
        self.assertEqual(self.user_service.get_user("test_username").full_name, "test_full_name")

    def test_get_user(self):
        """
        Test the get_user method.
        :return:
        """
        user_data = {
            "username": "test_username",
            "password": "test_password",
            "email": "test_email",
            "full_name": "test_full_name",
            "status": 1
        }
        self.user_service.create_user(user_data)
        self.assertEqual(self.user_service.get_user("test_username").username, "test_username")
        self.assertEqual(self.user_service.get_user("test_username").password, "test_password")
        self.assertEqual(self.user_service.get_user("test_username").email, "test_email")
        self.assertEqual(self.user_service.get_user("test_username").full_name, "test_full_name")

    def test_get_all_users(self):
        """
        Test the get_all_users method.
        :return:
        """
        user1_data = {
            "username": "test_username1",
            "password": "test_password1",
            "email": "test_email1",
            "full_name": "test_full_name1",
            "status": 1
        }

        user2_data = {
            "username": "test_username2",
            "password": "test_password2",
            "email": "test_email2",
            "full_name": "test_full_name2",
            "status": 1
        }

        self.user_service.create_user(user1_data)
        self.user_service.create_user(user2_data)
        users = self.user_service.get_all_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, "test_username1")
        self.assertEqual(users[1].username, "test_username2")

    def test_update_user(self):
        """
        Test the update_user_status method.
        :return:
        """
        user_data = {
            "username": "test_username",
            "password": "test_password",
            "email": "test_email",
            "full_name": "test_full_name",
            "status": 1
        }
        self.user_service.create_user(user_data)
        user_data = {
            "username": "test_username",
            "password": "test_password",
            "email": "test_email",
            "full_name": "new_full_name",
            "status": 1
        }
        self.user_service.update_user_status("test_username", user_data)
        self.assertEqual(self.user_service.get_user("test_username").full_name, "new_full_name")
