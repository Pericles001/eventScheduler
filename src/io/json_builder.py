"""
File: json_builder.py
Class: JsonBuilder - represents the builder for the event object based on a json file
"""
import json

import src.io.builder as builder
from src.model.event import Event
from src.repository import repository as repo


class JsonBuilder(builder.Builder):
    """
    Class: JsonBuilder
    Purpose: represents the builder for the event object based on a json file
    """

    def __init__(self):
        """
        Initialize a new json builder.

        """
        super().__init__()

    def build_event(self, file):
        """
        Build an event object based on a json file.

        Args:
            file (string): The file to build the event from.
        """
        return self.__build_event(file)

    def __build_event(self, file):
        """
        Function: __build_event
        Purpose: build an event object based on a json file.
        :param file:
        :return:
        """
        # open the file
        with open(file, "r") as f:
            # read the file
            data = json.load(f)
            events = []
            for event_data in data:
                # create a new event object
                event = Event(event_data["title"], event_data["date"], event_data["description"])
                # add the event to the list
                events.append(event)
            # return the event list
            print(event)
            return events
