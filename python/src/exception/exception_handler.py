"""
File: exception_handler.py
Class: ExceptionHandler - contains the exception handler for the event object.
"""


class ExceptionHandler:
    """
    Class: ExceptionHandler
    Purpose: contains the exception handler for the event object.
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle an exception.

        Args:
            exception (Exception): The exception to handle.
            :param exception: the exception to handle
            :param target: the input value that caused the exception
        """
        print(exception)
        return str(exception)