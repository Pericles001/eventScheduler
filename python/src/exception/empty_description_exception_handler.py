"""
File: empty_description_exception_handler.py
Class: EmptyDescriptionExceptionHandler - contains the exception handler for the event object - specifically for an empty description.
"""

from python.src.exception.exception_handler import ExceptionHandler


class EmptyDescriptionExceptionHandler(ExceptionHandler):
    """
    Class: EmptyDescriptionExceptionHandler
    Purpose: contains the exception handler for the event object - specifically for an empty description.
    - inherits from ExceptionHandler
    - override the handle_exception method to handle the empty description exception
    """

    @staticmethod
    def handle_exception(exception, target):
        """
        Handle the empty description exception.

        Args:
            exception (Exception): The empty description exception to handle.
            :param exception: the empty description exception to handle
            :param target: the input description value that caused the exception
        """
        print(exception)
        # generate a random description
        print("The description value is empty, generating a random description...")
        target = "Description" + str(hash(target))
        return target
