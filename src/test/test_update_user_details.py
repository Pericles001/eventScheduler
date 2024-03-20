"""
File: test_update_user_details.py
Description: Unit test for updating user details.
"""

import unittest

from src.io.user_save import SaveUser
from src.model.user import User
from src.service.users_service import UserService


class TestUpdateUserDetails(unittest.TestCase):

    def setUp(self):
        self.save_user = SaveUser()
        self.user_service = UserService()

    def test_update_user_details(self):
        user = User("test_user", "test_password", "test_email", "test_full_name", status=0, events=[])

        self.save_user.save_user(user)
        new_user_infos = {
            "username": "test_user_1",
            "password": "new_password_1",
            "email": "new_email_1",
            "full_name": "new_full_name_1",
            "status": 1
        }

        user_updates = [
            {"username": "test_user"},
            {"password": "new_password_1"},
            {"email": "new_email_1"},
            {"full_name": "new_full_name_1"},
            {"status": 1}
        ]

        self.user_service.update_user_details(user_updates)
        updated_user = self.user_service.get_user("test_user_1")
        self.assertEqual(updated_user.username, new_user_infos["username"])
        self.assertEqual(updated_user.email, new_user_infos["email"])
        self.assertEqual(updated_user.full_name, new_user_infos["full_name"])
