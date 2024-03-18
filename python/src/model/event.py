#!/usr/bin/python3
"""
File: event.py
Class: Event - represents an event in the scheduler system.
"""
import datetime

import python.src.exception.bad_datetype_exception_handler as bdteh
import python.src.exception.bad_titletype_exception_handler as bnte
import python.src.exception.bad_type_description_exception_handler as btdh
import python.src.exception.empty_date_exception_handler as edeh
import python.src.exception.empty_description_exception_handler as edeh
import python.src.exception.empty_title_exception_handler as eneh
import python.src.exception.past_date_exception_handler as pdeh


class Event:
    """
    Class: Event
    Purpose: contains the attributes of the event object.
    """

    def __init__(self, title, date, description):
        """
        Initialize a new event.

        Args:
            title (string): The title of the event.
            date (datetime [yyyy-mm-dd]): represents the date of the event in the format yyyy-mm-dd.
            description (string): description of the event.
        """
        self.title = title
        self.date = date
        self.description = description

    @property
    def title(self):
        """
        Get/set the name of the event
        :return: current name
        """
        return self.__title

    @title.setter
    def title(self, value):
        """
        :param value: 
        :return: 
        """
        try:
            if isinstance(value, str):
                if value == "":
                    raise ValueError("title cannot be empty")
                self.__title = value
            else:
                raise TypeError("title must be a string")
        except ValueError as ve:
            eneh.EmptyNameExceptionHandler.handle_exception(ve, value)
            self.__title = value
        except TypeError as te:
            bnte.BadNameTypeExceptionHandler.handle_exception(te, value)
            self.__title = value

    @property
    def date(self):
        """
        Get/set the date of the event
        :return: current date
        """
        return self.__date

    @date.setter
    def date(self, value):
        """
        :param value:
        :return:
        """
        current_date = datetime.date.today()
        try:
            if isinstance(value, datetime.date):
                if value < current_date:
                    raise ValueError("Date cannot be in the past")
                self.__date = value
            elif isinstance(value, str):
                parsed_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                if parsed_date < current_date:
                    raise ValueError("Date cannot be in the past")
                self.__date = parsed_date
            else:
                raise TypeError("Date must be a datetime.date object or a string in format 'yyyy-mm-dd'")
        except ValueError as ve:
            pdeh.PastDateExceptionHandler.handle_exception(ve, value)
            self.__date = value
        except TypeError as te:
            bdteh.BadDateTypeExceptionHandler.handle_exception(te, value)
            self.__date = value

    @property
    def description(self):
        """
        Get/set the description of the event
        :return:
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        :param value:
        :return:
        """
        try:
            if value == "":
                raise ValueError("Description cannot be empty")
            elif not isinstance(value, str):
                raise TypeError("Description must be a string")
            self.__description = value
        except ValueError as ve:
            edeh.EmptyDescriptionExceptionHandler.handle_exception(ve, value)
            self.__description = value
        except TypeError as te:
            btdh.BadTypeDescriptionExceptionHandler.handle_exception(te, value)
            self.__description = value


def print_event(event):
    """
    Function to print the event in a table display.
    :param event:
    :return:
    """
    print(f"{event.name:20} | {event.date} | {event.description}")


def __str__(self):
    """
    Define the string representation of the event.
    :param self:
    :return:
    """
    return f"{self.name} on {self.date} - {self.description}"
