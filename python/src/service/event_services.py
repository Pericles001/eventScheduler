#!/usr/bin/python3
"""
File: event_services.py
Class: EventServices - contains the services for the event object  (operations on the event object).
"""


class EventServices:
    """
    Class: EventServices
    Purpose: contains the services for the event object.
    """

    def __init__(self, event_repo):
        """
        Initialize a new event service.

        Args:
            event_repo (EventRepository): The event repository.
        """
        self.event_repo = event_repo

    def add_event(self, event):
        """
        Add a new event to the repository.

        Args:
            event (Event): The event to add.
        """
        self.event_repo.add_event(event)

    def get_event(self, name):
        """
        Get an event from the repository.

        Args:
            name (string): The name of the event to get.
        """
        return self.event_repo.get_event(name)

    def get_all_events(self):
        """
        Get all events from the repository.
        """
        return self.event_repo.get_all_events()

    def update_event(self, name, event):
        """
        Update an event in the repository.

        Args:
            name (string): The name of the event to update.
            event (Event): The updated event.
        """
        self.event_repo.update_event(name, event)

    def delete_event(self, name):
        """
        Delete an event from the repository.

        Args:
            name (string): The name of the event to delete.
        """
        self.event_repo.delete_event(name)


