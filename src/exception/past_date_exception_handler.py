"""
File: past_date_exception_handler.py
Class: PastDateExceptionHandler - contains the exception handler for the event object - specifically for a past date.
"""

from datetime import datetime, timedelta

import src


class PastDateExceptionHandler(src.exception.exception_handler.ExceptionHandler):
    """
    Class: PastDateExceptionHandler
    Purpose: contains the exception handler for the event object - specifically for a past date.
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the past date exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the past date exception.

        Args:
            exception (Exception): The past date exception to handle.
            :param exception: the past date exception to handle
            :param target: the input date value that caused the exception
        """
        print(exception)
        # generate a random date
        print("The date value is in the past, generating a random date...")
        # generate a date one week ahead of now
        current_date = datetime.now().date()
        target = current_date + timedelta(days=7)
        return target
