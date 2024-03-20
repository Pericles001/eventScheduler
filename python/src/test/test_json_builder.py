"""
File: test_json_builder.py
Purpose: contains the tests for the json builder.
"""

import unittest
from datetime import datetime

from python.src.io.json_builder import JsonBuilder


class TestJsonBuilder(unittest.TestCase):
    """
    Class: TestJsonBuilder
    Purpose: contains the tests for the json builder.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.json_builder = JsonBuilder()

    def test_build_json(self):
        """
        Method: test_build_json
        Purpose: tests the build_json method.
        """
        file = "../../data/in/event_data.json"
        events = self.json_builder.build_event(file)
        # display the events
        for event in events.events:
            print(event.title, event.date, event.description)
        # check the events
        self.assertEqual(len(events.events), 3)
        self.assertEqual(events.events[0].title, "Birthday Celebration")
        self.assertEqual(events.events[0].date, datetime(2024, 11, 10))
        self.assertEqual(events.events[0].description, "Surprise party! Decorations, cake, and games.")
        self.assertEqual(events.events[1].title, "Test Event 2")
        self.assertEqual(events.events[1].date, datetime(2020, 1, 2))
        self.assertEqual(events.events[1].description, "This is a test event 2")
        self.assertEqual(events.events[2].title, "Test Event 3")
        self.assertEqual(events.events[2].date, datetime(2020, 1, 3))
        self.assertEqual(events.events[2].description, "This is a test event 3")
