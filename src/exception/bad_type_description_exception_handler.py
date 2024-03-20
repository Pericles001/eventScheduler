"""
File: bad_type_description_exception_handler.py
Class: BadTypeDescriptionExceptionHandler - contains the exception handler for the description type exception (when the value is not a string).
"""

from src.exception.exception_handler import ExceptionHandler


class BadTypeDescriptionExceptionHandler(ExceptionHandler):
    """
    Class: BadTypeDescriptionExceptionHandler
    Purpose: contains the exception handler for the description type exception (when the value is not a string).
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the description type exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the description type exception.

        Args:
            exception (Exception): The description type exception to handle.
            :param exception: the description type exception to handle
            :param target: the input description value that caused the exception
        """
        print(exception)
        # transform the target value to a string
        target = str(target)
        print("The target value has been transformed to a string...")
        return target
