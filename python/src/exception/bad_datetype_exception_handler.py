"""
File: bad_datetype_exception_handler.py
Class: BadDateTypeExceptionHandler - contains the exception handler for the date type exception (when the value is not datetime.date).
- inherits from ExceptionHandler
"""
from datetime import datetime

from python.src.exception.exception_handler import ExceptionHandler


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

        # find the type of the target
        target_type = type(target)
        if target_type == str:
            #     transform the target value to a datetime object ("yyyy-mm-dd" to datetime.date)
            target = datetime.strptime(target, "%Y-%m-%d").date()
            print("The target value has been transformed to a datetime object...")
            return target
        else:
            # generate a random date in the future week
            print("The target value is not a string, generating a random date in the future week...")
            target = datetime.now().date()
            return target
