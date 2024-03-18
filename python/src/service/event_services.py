#!/usr/bin/python3
"""
File: event_services.py
Class: EventServices - contains the services for the event object  (operations on the event object).
"""

from datetime import datetime, timedelta
import python.src.repository.repository as repo
import python.src.model.event as event
import python.src.io.json_builder
import python.src.io.flat_builder


class EventServices:
    """
    Class: EventServices
    Purpose: contains the services for the event object  (operations on the event object).
    """

    def __init__(self):
        self.repo = repo.EventRepository()

    def create_event(self, title, date, description):
        """
        Create a new event.

        Args:
            title (string): The title of the event.
            date (datetime [yyyy-mm-dd]): represents the date of the event in the format yyyy-mm-dd.
            description (string): description of the event.
        :param title:
        :param date:
        :param description:
        :return:
        """
        try:
            new_event = event.Event(title, date, description)
            self.repo.add_event(new_event)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_all_events(self):
        """
        Get all events from the repository.
        """
        try:
            return self.repo.get_all_events()
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_event(self, title):
        """
        Get an event from the repository.

        Args:
            title (string): The name of the event to get.
        """
        try:
            return self.repo.get_event(title)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_event_string(self, title):
        """
        Get an event from the repository.

        Args:
            title (string): The name of the event to get.
        """
        try:
            target_event = self.repo.get_event(title)
            return "Title: " + target_event.title + "\nDate: " + target_event.date + "\nDescription: " + target_event.description
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
            return None

    def get_all_events(self):
        """
        Get all events from the repository.
        """
        try:
            return self.repo.get_all_events()
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_all_events_string(self):
        """
        Get all events from the repository.
        """
        try:
            events = self.repo.get_all_events()
            result = ""
            for event in events:
                result += "Title: " + event.title + "\nDate: " + event.date + "\nDescription: " + event.description + "\n\n"
            return result
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
            return None

    def update_event(self, title, new_title, new_date, new_description):
        """
        Update an event in the repository.

        Args:
            title (string): The name of the event to update.
            new_title (string): The new title of the event.
            new_date (datetime [yyyy-mm-dd]): represents the new date of the event in the format yyyy-mm-dd.
            new_description (string): new description of the event.
        """
        try:
            target_event = self.repo.get_event(title)
            target_event.title = new_title
            target_event.date = new_date
            target_event.description = new_description
            self.repo.update_event(title, target_event)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def delete_event(self, title):
        """
        Delete an event from the repository.

        Args:
            title (string): The name of the event to delete.
        """
        try:
            self.repo.delete_event(title)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_events_by_year(self, year):
        """
        Get all events from the repository for a given year.

        Args:
            year (int): The year to get the events for.
            :param self:
        """
        try:
            events = self.repo.get_all_events()
            result = []
            for event in events:
                if event.date.year == year:
                    result.append(event)
            return result
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def create_event_json(self, filepath):
        """
        Method: create_event_json
        Purpose: creates an event from a json file.
        """
        try:
            json_builder = python.src.io.json_builder.JsonBuilder()
            json_builder.build_event(filepath)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        finally:
            print("Event created from json file")

    def create_event_flat(self, filepath):
        """
        Method: create_event_flat
        Purpose: creates an event from a flat file.
        """
        try:
            flat_builder = python.src.io.flat_builder.FlatBuilder()
            flat_builder.build_event(filepath)
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        finally:
            print("Event created from flat file")
