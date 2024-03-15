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

    def get_event(self, name):
        """
        Get an event from the repository.

        Args:
            name (string): The name of the event to get.
        """
        for event in self.events:
            if event.name == name:
                return event
        return None

    def get_all_events(self):
        """
        Get all events from the repository.
        """
        return self.events

    def update_event(self, name, event):
        """
        Update an event in the repository.

        Args:
            name (string): The name of the event to update.
            event (Event): The updated event.
        """
        for i in range(len(self.events)):
            if self.events[i].name == name:
                self.events[i] = event
                return

    def delete_event(self, name):
        """
        Delete an event from the repository.

        Args:
            name (string): The name of the event to delete.
        """
        for i in range(len(self.events)):
            if self.events[i].name == name:
                del self.events[i]
                return
