"""
File: test_event_repository.py
Class: TestEventRepository - contains the tests for the event repository.
"""

import unittest
from python.src.model.event import Event
from python.src.repository.repository import EventRepository


class TestEventRepository(unittest.TestCase):
    """
    Class: TestEventRepository
    Purpose: contains the tests for the event repository.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.event_repo = EventRepository()
        self.event1 = Event("Test Event 1", "2020-01-01", "This is a test event 1")
        self.event2 = Event("Test Event 2", "2020-01-02", "This is a test event 2")

    def test_add_event(self):
        """
        Test adding an event to the repository.
        """
        self.event_repo.add_event(self.event1)
        self.assertEqual(len(self.event_repo.events), 1)
        self.assertEqual(self.event_repo.events[0], self.event1)

    def test_get_event(self):
        """
        Test getting an event from the repository.
        """
        self.event_repo.add_event(self.event1)
        self.assertEqual(self.event_repo.get_event("Test Event 1"), self.event1)

    def test_get_all_events(self):
        """
        Test getting all events from the repository.
        """
        self.event_repo.add_event(self.event1)
        self.event_repo.add_event(self.event2)
        self.assertEqual(self.event_repo.get_all_events(), [self.event1, self.event2])

    def test_update_event(self):
        """
        Test updating an event in the repository.
        """
        self.event_repo.add_event(self.event1)
        self.event_repo.update_event("Test Event 1", self.event2)
        self.assertEqual(self.event_repo.get_event("Test Event 2"), self.event2)

    def test_delete_event(self):
        """
        Test deleting an event from the repository.
        """
        self.event_repo.add_event(self.event1)
        self.event_repo.delete_event("Test Event 1")
        self.assertEqual(self.event_repo.get_event("Test Event 1"), None)
