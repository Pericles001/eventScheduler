"""
File: bad_datetype_exception_handler.py
Class: BadDateTypeExceptionHandler - contains the exception handler for the date type exception (when the value is not datetime.date).
- inherits from ExceptionHandler
"""
from datetime import datetime, timedelta

from src.exception.exception_handler import ExceptionHandler


class BadDateTypeExceptionHandler(ExceptionHandler):
    """
    Class: BadDateTypeExceptionHandler
    Purpose: contains the exception handler for the date type exception (when the value is not datetime.date).
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the date type exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the date type exception.

        Args:
            exception (Exception): The date type exception to handle.
            :param exception: the date type exception to handle
            :param target: the input date value that caused the exception
        """
        print(exception)
        # check if the target value is a datetime.date object
        if not isinstance(target, datetime.date):
            # If the input IS NOT 'datetime.date' we need to handle it
            if isinstance(target, datetime.datetime):
                # Convert the 'datetime.datetime' object to 'datetime.date'
                target = target.date()
                print("The target value has been transformed to a datetime.date object...")
            elif isinstance(target, str):
                # Transform string (as before)
                target = datetime.strptime(target, "%Y-%m-%d").date()
                print("The target value has been transformed to a datetime object...")
            else:
                # Handle other incorrect types (e.g., generate random date)
                print("The target value is not a supported date type, generating a random date in the future week...")
                current_date = datetime.now().date()
                target = current_date + timedelta(days=7)

        return target
