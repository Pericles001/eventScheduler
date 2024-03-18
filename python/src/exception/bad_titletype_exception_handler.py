"""
File: bad_titletype_exception_handler.py
Class: BadNameTypeExceptionHandler - contains the exception handler for the name type exception (when the value is not a string).
"""

from python.src.exception.exception_handler import ExceptionHandler


class BadNameTypeExceptionHandler(ExceptionHandler):
    """
    Class: BadNameTypeExceptionHandler
    Purpose: contains the exception handler for the name type exception (when the value is not a string).
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the name type exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the name type exception.

        Args:
            exception (Exception): The name type exception to handle.
            :param exception: the name type exception to handle
            :param target: the input name value that caused the exception
        """
        print(exception)
        # transform the target value to a string
        target = str(target)
        print("The target value has been transformed to a string...")
        return target
