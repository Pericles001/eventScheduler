"""
File: empty_date_exception_handler.py
Class: EmptyDateExceptionHandler - contains the exception handler for the event object - specifically for an empty date.
"""
from datetime import timedelta, datetime

from src.exception.exception_handler import ExceptionHandler


class EmptyDateExceptionHandler(ExceptionHandler):
    """
    Class: EmptyDateExceptionHandler
    Purpose: contains the exception handler for the event object - specifically for an empty date.
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the empty date exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the empty date exception.

        Args:
            exception (Exception): The empty date exception to handle.
            :param exception: the empty date exception to handle
            :param target: the input date value that caused the exception
        """
        print(exception)
        # generate a random date
        print("The date value is empty, generating a random date...")
        # generate a date one week ahead of now
        current_date = datetime.now().date()
        target = current_date + timedelta(days=7)
        return target
