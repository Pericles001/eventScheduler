"""
File: test_flat_builder.py
Class: TestFlatBuilder - contains the tests for the flat builder.
"""

import unittest
from datetime import date

from python.src.io.flat_builder import FlatBuilder


class TestFlatBuilder(unittest.TestCase):
    """
    Class: TestFlatBuilder
    Purpose: contains the tests for the flat builder.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.flat_builder = FlatBuilder()

    def test_build_event(self):
        """
        Test building an event from a flat file.
        """
        file = "../../data/in/event_data.txt"
        events = self.flat_builder.build_event(file)
        # display the events
        for event in events.events:
            print(event.title, event.date, event.description)
        # check the events

        self.assertEqual(len(events.events), 3)
        self.assertEqual(events.events[0].title, "Birthday Celebration")
        self.assertEqual(events.events[0].date, date(2024, 11, 10))
        self.assertEqual(events.events[0].description, "Surprise party! Decorations, cake, and games.")
        self.assertEqual(events.events[1].title, "Test Event 2")
        self.assertEqual(events.events[1].date, "2020-01-02")
        self.assertEqual(events.events[1].description, "This is a test event 2")
