"""
File: main.py
Class: Main - the main class of the system
Purpose: Launches the application
"""

import src.ui.event_scheduler_ui as event_scheduler_ui


class Main:
    """
    Class: Main
    Purpose: the main class of the system
    """

    def __init__(self):
        """
        Initialize a new main class.
        """
        self.ui = event_scheduler_ui.EventSchedulerUI()
        self.ui.start()


if __name__ == "__main__":
    main = Main()
    main.ui.start()
