"""
File: empty_name_exception_handler.py
Class: EmptyNameExceptionHandler - contains the exception handler for the event object - specifically for an empty name.
"""
from python.src.exception.exception_handler import ExceptionHandler


class EmptyNameExceptionHandler(ExceptionHandler):
    """
    Class: EmptyNameExceptionHandler
    Purpose: contains the exception handler for the event object - specifically for an empty name.
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the empty name exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the empty name exception.

        Args:
            exception (Exception): The empty name exception to handle.
            :param exception: the empty name exception to handle
            :param target: the input name value that caused the exception
        """
        print(exception)
        # generate a random name
        print("The name value is empty, generating a random name...")
        target = "Event" + str(hash(target))
        return target