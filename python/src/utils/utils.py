"""
File: utils.py
Purpose: contains utility functions for the project
"""


def create_log_file_if_not_exists():
    """
    Create a log file if it does not exist.
    """
    import os
    import datetime

    today = datetime.datetime.now()
    log_file_name = today.strftime("%d_%m_%Y") + ".log"
    if not os.path.exists("logs"):
        os.makedirs("logs")
    if not os.path.exists("logs/" + log_file_name):
        with open("logs/" + log_file_name, "w") as f:
            f.write("Log file created on " + today.strftime("%d/%m/%Y %H:%M:%S"))
            f.close()
    return "logs/" + log_file_name


def write_to_daily_log_file(message, log_name):
    """
    Write a message to the daily log file.
    :param message: The message to write to the log file.
    :param log_name: The name of the log file to write to.
    :return: None
    """
    import datetime

    today = datetime.datetime.now()
    with open(log_name, "a") as f:
        f.write("\n" + today.strftime("%d/%m/%Y %H:%M:%S") + " - " + message)
        f.close()


def get_current_time():
    """
    Get the current time in the format "YYYY-MM-DD HH:MM:SS".
    """
    import datetime

    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def encrypt_password(password):
    """
    Encrypt a password using the SHA-256 algorithm.
    :param password: The password to encrypt.
    :return: The encrypted password.
    """
    import hashlib

    return hashlib.sha256(password.encode()).hexdigest()
