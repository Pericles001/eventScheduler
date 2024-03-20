"""
File: test_event.py
Class: TestEvent - contains the tests for creating and reading the event object.
"""

import unittest
from datetime import datetime

from src.model.event import Event


class TestEvent(unittest.TestCase):
    """
    Class: TestEvent
    Purpose: contains the tests for creating and reading the event object.
    """

    def test_create_event(self):
        """
        Test creating an event.
        """
        event = Event("Test Event", datetime(2020, 1, 1), "This is a test event")
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.date, datetime(2020, 1, 1))
        self.assertEqual(event.description, "This is a test event")

    def test_create_event_invalid_name(self):
        """
        Test creating an event with an invalid name.
        """
        with self.assertRaises(ValueError):
            Event("", datetime(2020, 1, 1), "This is a test event")

    def test_create_event_invalid_date(self):
        """
        Test creating an event with an invalid date.
        """
        with self.assertRaises(TypeError):
            Event("Test Event", "2020-01-01", "This is a test event")

    def test_create_event_invalid_description(self):
        """
        Test creating an event with an invalid description.
        """
        with self.assertRaises(TypeError):
            Event("Test Event", datetime.date(2020, 1, 1), 123)
