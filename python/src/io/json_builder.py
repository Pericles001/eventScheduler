"""
File: json_builder.py
Class: JsonBuilder - represents the builder for the event object based on a json file
"""

import python.src.io.builder as builder
from python.src.model.event import Event
from python.src.repository import repository as repo


class JsonBuilder(builder):
    """
    Class: JsonBuilder
    Purpose: represents the builder for the event object based on a json file
    """
    def __init__(self):
        pass

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
            data = f.read()
            #  the file has a format of [{
            #   "title": "The Shawshank Redemption",
            #     "date": "2024-04-01",
            #     "description": "Two imprisoned people trying to survive in a prison."
            # }, {
            #   "title": "The Shawshank Redemption",
            #     "date": "2024-04-01",
            #     "description": "Two imprisoned people trying to survive in a prison."
            # }]
            # convert the data to a list of dictionaries
            events = repo.EventRepository()
            for event in data:
                # create a new event object
                event = Event(event["title"], event["date"], event["description"])
                # add the event to the list
                events.add_event(event)
            # return the event list
            return events