#!/usr/bin/python3
"""
File: repository.py
Class: Repository for storing the event objects in a list of dictionaries.
"""


class EventRepository:
    """
    Class: EventRepository
    Purpose: contains the repository for the event object.
    """

    def __init__(self):
        """
        Initialize a new event repository.
        """
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the repository.

        Args:
            event (Event): The event to add.
        """
        self.events.append(event)

    def get_event(self, title):
        """
        Get an event from the repository.

        Args:
            title (string): The name of the event to get.
        """
        for event in self.events:
            if event.title == title:
                return event
        return None

    def get_all_events(self):
        """
        Get all events from the repository.
        """
        return self.events

    def update_event(self, title, event):
        """
        Update an event in the repository.

        Args:
            title (string): The name of the event to update.
            event (Event): The updated event.
        """
        for i in range(len(self.events)):
            if self.events[i].title == title:
                self.events[i] = event
                return

    def delete_event(self, title):
        """
        Delete an event from the repository.

        Args:
            title (string): The name of the event to delete.
        """
        for i in range(len(self.events)):
            if self.events[i].name == title:
                del self.events[i]
                return


class UserRepository:
    """
Class: UserRepository
Purpose: contains the repository for the user object.
"""

    def __init__(self):
        """
        Initialize a new user repository.
        """
        self.users = []

    def add_user(self, user):
        """
        Add a new user to the repository.

        Args:
            user (User): The user to add.
            :param user:
            :param self:
        """
        self.users.append(user)

    def get_user(self, username):
        """
        Get a user from the repository.
        :param self:
        :param username:
        :return:
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_all_users(self):
        """
        Get all users from the repository.
        """
        return self.users

    def update_user(self, username, user):
        """
        Update a user in the repository.
        :param self:
        :param username:
        :param user:
        :return:
        """
        for i in range(len(self.users)):
            if self.users[i].username == username:
                self.users[i] = user
                return

    def delete_user(self, username):
        """
        Delete a user from the repository.
        :param self:
        :param username:
        :return:
        """
        for i in range(len(self.users)):
            if self.users[i].username == username:
                del self.users[i]
                return

    def get_repo_length(self):
        """
        Get the length of the repository.
        :param self:
        :return:
        """
        return len(self.users)

    def get_user_by_username(self, username):
        """
        Get a user from the repository by username.
        :param username:
        :return:
        """
        for user in self.users:
            if user.username == username:
                return user
        return None
