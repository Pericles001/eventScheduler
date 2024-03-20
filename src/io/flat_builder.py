"""
File: flat_builder
Class: FlatBuilder - represents the builder for the event object based on a flat file (txt), inherits from the Builder class.
"""

import src.io.builder as builder
from src.model.event import Event
from src.repository import repository as repo


class FlatBuilder(builder.Builder):
    """
    Class: FlatBuilder
    Purpose: represents the builder for the event object based on a flat file (txt), inherits from the Builder class.
    """

    def __init__(self):
        """
        Initialize a new flat builder.
        """
        super().__init__()

    def build_event(self, file):
        """
        Build an event object based on a flat file.

        Args:
            file (string): The file to build the event from.
        """
        return self.__build_event(file)

    def __build_event(self, file):
        """
        Function: __build_event
        Purpose: build an event object based on a flat file.
        :param file:
        :return: an EventRepository object containing the created events
        """
        # open the file
        with open(file, "r") as f:
            # read the file
            lines = f.readlines()
            # initialize the event list
            events = []
            # for each line in the file
            for line in lines:
                # each line is one event: title; date; description (comma separated values)
                parts = line.strip().split("; ")
                # Print the parts to debug
                print("Parts:", parts)
                # Check if the line has the expected number of parts
                if len(parts) != 3:
                    print("Invalid format in line:", line)
                    continue  # Skip to the next line
                title = parts[0].split(": ")[1]  # Extract title from the format "Title: <title>"
                date = parts[1].split(": ")[1]  # Extract date from the format "Date: yyyy-mm-dd"
                description = parts[2].split(": ")[
                    1]  # Extract description from the format "Description: <description>"
                # create a new event object
                event = Event(title, date, description)
                # add the event to the list
                events.append(event)
        # return the event list
        return events
