"""
File: event_scheduler_ui.py
Class: EventSchedulerUI
Purpose: contains the user interface for the event scheduler application.
"""

import python.src.service.users_service as user_service
import python.src.service.event_services as event_service


def register_user():
    """
    Method: register_user
    Purpose: displays the registration form.
    """
    print("Enter the user details:")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    full_name = input("Full Name: ")
    status = 0
    while True:
        print("Are you sure you want to register?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                user_data = {
                    "username": username,
                    "password": password,
                    "email": email,
                    "full_name": full_name,
                    "status": status
                }
                user_service.UserService().create_user(user_data)
                print("User registered successfully!")
                # user_service.UserService().save_user_details(user_data)  # Pass user_data here
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


# def login_user():
#     """
#     Method: login_user
#     Purpose: displays the login form.
#     """
#     print("Enter the user details:")
#     username = input("Username: ")
#     password = input("Password: ")
#     while True:
#         print("Are you sure you want to login?")
#         print("1. Yes")
#         print("2. No")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             user_data = {
#                 "username": username,
#                 "password": password
#             }
#             user_service.UserService().login_user(user_data)
#             main_menu()
#             break
#         elif choice == "2":
#             break
#         else:
#             print("Invalid choice! Please try again.")

def login_user():
    """
    Method: login_user
    Purpose: displays the login form.
    """
    print("Enter the user details:")
    username = input("Username: ")
    password = input("Password: ")
    while True:
        print("Are you sure you want to login?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            user_data = {
                "username": username,
                "password": password
            }
            logged_in_user = user_service.UserService().login_user(user_data)
            if logged_in_user:
                main_menu()  # Pass the logged-in user to the main menu
            break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def main_menu():
    """
    Method: main_menu
    Purpose: displays the main menu.
    """
    print("1. Create Event")
    print("2. View Event")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Logout")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            submenu_create_event_category()
        elif choice == "2":
            submenu_view_event()
        elif choice == "3":
            submenu_update_event()
        elif choice == "4":
            submenu_delete_event()
        elif choice == "5":
            submenu_logout()
            break
        else:
            print("Invalid choice! Please try again.")


def auth_menu():
    """
    Method: auth_menu
    Purpose: displays the authentication menu.
    """
    print("Welcome to the Event Scheduler!")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_create_event_category():
    """
    Method: submenu_create_event_category
    :return:
    """
    print("1. Import Event details from a file")
    print("2. Enter Event details manually")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            submenu_create_event_file()
        elif choice == "2":
            submenu_create_event_manual()
        else:
            print("Invalid choice! Please try again.")


def submenu_create_event_manual():
    """
    Method: submenu_create_event_manual
    Purpose: displays the submenu for creating an event manually.
    """
    print("Enter the event details:")
    title = input("Title: ")
    date = input("Date: (yyyy-mm-dd)")
    description = input("Description: ")
    while True:
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                event_data = {
                    "title": title,
                    "date": date,
                    "description": description
                }
                event_service.EventServices.create_event(title, date, description)
                print("Event created successfully!")
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_create_event_file():
    """
    Method: submenu_create_event_file
    Purpose: displays the submenu for creating an event from a file.
    """
    print("1. Import the event details from a json file:")
    print("2. Import the event details from a flat file:")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            submenu_create_event_json()
        elif choice == "2":
            submenu_create_event_flat()
        else:
            print("Invalid choice! Please try again.")


def submenu_create_event_json():
    """
    Method: submenu_create_event_json
    Purpose: displays the submenu for creating an event from a json file.
    """
    print("Enter the file path:")
    file_name = input("File path: ")
    while True:
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                event_service.EventServices.create_event_json(file_name)
                print("Event created successfully!")
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")
    return file_name


def submenu_create_event_flat():
    """
    Method: submenu_create_event_flat
    Purpose: displays the submenu for creating an event from a flat file.
    """
    print("Enter the file path:")
    file_name = input("File path: ")
    while True:
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                event_service.EventServices.create_event_flat(file_name)
                print("Event created successfully!")
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_view_event():
    """
    Method: submenu_view_event
    Purpose: displays the submenu for viewing an event.
    """
    print("1. View all events")
    print("2. View a specific event")
    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            event_service.EventServices.get_all_events()
            break
        elif choice == "2":
            submenu_view_specific_event()
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_view_specific_event():
    print("Enter the event title:")
    title = input("Title: ")
    while True:
        print("Are you sure you want to view the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            event_service.EventServices.get_event(title)
            break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_update_event():
    """
    Method: submenu_update_event
    Purpose: displays the submenu for updating an event.
    """
    print("Enter the event title: ")
    old_title = input("Title: ")
    print("Enter the updated event details:")
    title = input("Title: ")
    date = input("Date: (yyyy-mm-dd)")
    description = input("Description: ")
    while True:
        print("Are you sure you want to update the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                event_service.EventServices.update_event(old_title, title, date, description)
                print("Event updated successfully!")
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_delete_event():
    """
    Method: submenu_delete_event
    Purpose: displays the submenu for deleting an event.
    """
    print("Enter the event title:")
    title = input("Title: ")
    while True:
        print("Are you sure you want to delete the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                event_service.EventServices.delete_event(title)
                print("Event deleted successfully!")
                break
            except Exception as e:
                print("Error: ", e)
                break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


def submenu_logout():
    """
    Method: submenu_logout
    Purpose: displays the submenu for logging out.
    """
    print("Are you sure you want to logout?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            user_service.UserService().logout_user()
            break
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please try again.")


class EventSchedulerUI:
    """
    Class: EventSchedulerUI
    Purpose: contains the user interface for the event scheduler application.
    """

    def __init__(self):
        """
        Initialize the event scheduler UI.
        """
        pass

    def start(self):
        """
        Start the event scheduler UI.
        """
        #  load the users in the user repository
        user_service.UserService().load_users()
        auth_menu()
        pass
