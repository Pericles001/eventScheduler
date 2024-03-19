"""
File: event_scheduler_ui.py
Class: EventSchedulerUI
Purpose: contains the user interface for the event scheduler application.
"""

import python.src.service.users_service as user_service
import python.src.service.event_services as event_service
import python.src.utils.utils as utils

daily_log_file = utils.create_log_file_if_not_exists()

logged_in_user = None  # Global variable to store the logged-in user
sys_users = user_service.UserService().load_users()


def register_user():
    """
    Method: register_user
    Purpose: displays the registration form and call the function to register a user.
    """
    utils.write_to_daily_log_file("User registration function: CALL ", daily_log_file)
    global sys_users  # To access the global variable
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
        utils.write_to_daily_log_file("User registration function: CHOICE " + choice, daily_log_file)
        if choice == "1":
            try:
                user_data = {
                    "username": username,
                    "password": password,
                    "email": email,
                    "full_name": full_name,
                    "status": status,
                    "events": []
                }
                # check if there is already a user with the same username
                if user_service.UserService().get_user(sys_users, username):
                    print("User already exists!")
                    utils.write_to_daily_log_file("User registration function: User already exists ", daily_log_file)
                    break
                user_service.UserService().create_user(user_data)
                utils.write_to_daily_log_file("User registration function: User created successfully ", daily_log_file)
                break
            except Exception as e:
                print("Error: ", e)
                utils.write_to_daily_log_file("User registration function: Error " + str(e), daily_log_file)
                break

        elif choice == "2":
            utils.write_to_daily_log_file("User registration function: User registration cancelled ", daily_log_file)
            main_menu()
        else:
            utils.write_to_daily_log_file("User registration function: Invalid choice ", daily_log_file)
            print("Invalid choice! Please try again.")


def login_user():
    """
    Method: login_user
    Purpose: displays the login form.
    """
    utils.write_to_daily_log_file("User login function: CALL ", daily_log_file)
    global logged_in_user  # To modify the global variable
    print("Enter the user details:")
    username = input("Username: ")
    password = input("Password: ")
    utils.write_to_daily_log_file("User login function: Username " + username, daily_log_file)
    while True:
        print("Are you sure you want to login?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        utils.write_to_daily_log_file("User login function: CHOICE " + choice, daily_log_file)
        if choice == "1":
            user_data = {
                "username": username,
                "password": password
            }
            logged_in_user = user_service.UserService().login_user(user_data)
            if logged_in_user:
                print(logged_in_user)
                utils.write_to_daily_log_file("User login function: User logged in successfully " +
                                              str(logged_in_user), daily_log_file)
                main_menu()  # Pass the logged-in user to the main menu
            break
        elif choice == "2":
            utils.write_to_daily_log_file("User login function: User login cancelled ", daily_log_file)
            main_menu()
        else:
            print("Invalid choice! Please try again.")
            utils.write_to_daily_log_file("User login function: Invalid choice ", daily_log_file)
    return logged_in_user


def main_menu():
    """
    Method: main_menu
    Purpose: displays the main menu.
    """
    utils.write_to_daily_log_file("Main menu function: CALL ", daily_log_file)
    global logged_in_user  # To access the global variable
    print("1. Create Event")
    print("2. View Event")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Logout")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Main menu function: Create event ", daily_log_file)
            submenu_create_event_category()
        elif choice == "2":
            utils.write_to_daily_log_file("Main menu function: View event ", daily_log_file)
            submenu_view_event()
        elif choice == "3":
            utils.write_to_daily_log_file("Main menu function: Update event ", daily_log_file)
            submenu_update_event()
        elif choice == "4":
            utils.write_to_daily_log_file("Main menu function: Delete event ", daily_log_file)
            submenu_delete_event()
        elif choice == "5":
            utils.write_to_daily_log_file("Main menu function: Logout ", daily_log_file)
            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("Main menu function: Invalid choice ", daily_log_file)
            print("Invalid choice! Please try again.")


def return_to_main_menu():
    """
Method: return_to_main_menu
Purpose: returns the user to the main menu.
"""
    utils.write_to_daily_log_file("Return to main menu function: CALL ", daily_log_file)
    print("1. Return to main menu")
    print("2. Logout")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Return to main menu function: Return to main menu ", daily_log_file)
            main_menu()
            break
        elif choice == "2":
            utils.write_to_daily_log_file("Return to main menu function: Logout ", daily_log_file)
            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("Return to main menu function: Invalid choice ", daily_log_file)
            print("Invalid choice! Please try again.")


def auth_menu():
    """
    Method: auth_menu
    Purpose: displays the authentication menu.
    """
    utils.write_to_daily_log_file("Authentication menu function: CALL ", daily_log_file)
    print("Welcome to the Event Scheduler!")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Authentication menu function: Login ", daily_log_file)
            login_user()
        elif choice == "2":
            utils.write_to_daily_log_file("Authentication menu function: Register ", daily_log_file)
            register_user()
        elif choice == "3":
            utils.write_to_daily_log_file("Authentication menu function: Exit ", daily_log_file)
            print("Goodbye!")
            exit(0)
        else:
            utils.write_to_daily_log_file("Authentication menu function: Invalid choice ", daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_create_event_category():
    """
    Method: submenu_create_event_category
    :return:
    """
    utils.write_to_daily_log_file("Create event category function: CALL ", daily_log_file)
    print("1. Import Event details from a file")
    print("2. Enter Event details manually")
    print("3. Return to main menu")
    print("4. Logout")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Create event category function: Import event details from a file - User:" +
                                          str(logged_in_user), daily_log_file)
            submenu_create_event_file()
        elif choice == "2":
            utils.write_to_daily_log_file("Create event category function: Enter event details manually - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_create_event_manual()
        elif choice == "3":
            utils.write_to_daily_log_file("Create event category function: Return to main menu - User" +
                                          str(logged_in_user), daily_log_file)
            return_to_main_menu()
        elif choice == "4":
            utils.write_to_daily_log_file("Create event category function: Logout - User" +
                                          str(logged_in_user), daily_log_file)

            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("Create event category function: Invalid choice - User" +
                                          str(logged_in_user), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_create_event_manual():
    """
    Method: submenu_create_event_manual
    Purpose: displays the submenu for creating an event manually.
    """
    utils.write_to_daily_log_file("Create event manually function: CALL ", daily_log_file)
    print("Enter the event details:")
    title = input("Title: ")
    date = input("Date: (yyyy-mm-dd)")
    description = input("Description: ")
    while True:
        utils.write_to_daily_log_file("Create event manually function: User " + str(logged_in_user) + "Details: " +
                                      str(title) + ", " + str(date) + ", "
                                      + str(description), daily_log_file)
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Create event manually function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            try:
                event_data = {
                    "title": title,
                    "date": date,
                    "description": description
                }
                datafile = "data/out/users.json"
                event_service_instance = event_service.EventServices()
                event_service_instance.create_event(title, date, description, logged_in_user.username, sys_users,
                                                    datafile)
                utils.write_to_daily_log_file("Create event manually function: Event created successfully ",
                                              daily_log_file)
                main_menu()
                break
            except Exception as e:
                utils.write_to_daily_log_file("Create event manually function: Error " + str(e), daily_log_file)
                print("Error: ", e)
                main_menu()
                break
        elif choice == "2":
            utils.write_to_daily_log_file("Create event manually function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            print("Event not created.")
            submenu_create_event_category()
            break
        else:
            utils.write_to_daily_log_file("Create event manually function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_create_event_file():
    """
    Method: submenu_create_event_file
    Purpose: displays the submenu for creating an event from a file.
    """
    utils.write_to_daily_log_file("Create event from file function: CALL ", daily_log_file)
    print("1. Import the event details from a json file:")
    print("2. Import the event details from a flat file:")
    print("3. Return to main menu")
    print("4. Logout")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file(
                "Create event from file function: Import event details from a json file - User" +
                str(logged_in_user), daily_log_file)
            submenu_create_event_json()
        elif choice == "2":
            utils.write_to_daily_log_file(
                "Create event from file function: Import event details from a flat file - User" +
                str(logged_in_user), daily_log_file)
            submenu_create_event_flat()
        elif choice == "3":
            utils.write_to_daily_log_file("Create event from file function: Return to main menu - User" +
                                          str(logged_in_user), daily_log_file)
            return_to_main_menu()
        elif choice == "4":
            utils.write_to_daily_log_file("Create event from file function: Logout - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("Create event from file function: Invalid choice - User" +
                                          str(logged_in_user), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_create_event_json():
    """
    Method: submenu_create_event_json
    Purpose: displays the submenu for creating an event from a json file.
    """
    utils.write_to_daily_log_file("Create event from json function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    while True:
        file_name = input("Enter the file path: ")
        utils.write_to_daily_log_file("Create event from json function: File path " + str(file_name), daily_log_file)
        if file_name:
            print("Are you sure you want to create the event?")
            print("1. Yes")
            print("2. No")
            choice = input("Enter your choice: ")
            if choice == "1":
                utils.write_to_daily_log_file("Create event from json function: User " + str(logged_in_user) +
                                              "Choice: " + str(choice), daily_log_file)
                try:
                    datafile = "data/out/users.json"
                    event_service.EventServices().create_event_json(file_name, logged_in_user.username, sys_users,
                                                                    datafile)
                    utils.write_to_daily_log_file("Create event from json function: Event created successfully ",
                                                  daily_log_file)
                except Exception as e:
                    utils.write_to_daily_log_file("Create event from json function: Error " + str(e), daily_log_file)
                    print("Error:", e)
                main_menu()
                break
            elif choice == "2":
                utils.write_to_daily_log_file("Create event from json function: User " + str(logged_in_user) +
                                              "Choice: " + str(choice), daily_log_file)
                submenu_create_event_category()
                break
            else:
                utils.write_to_daily_log_file("Create event from json function: User " + str(logged_in_user) +
                                              "Choice: " + str(choice), daily_log_file)
                print("Invalid choice! Please try again.")
        else:
            utils.write_to_daily_log_file("Create event from json function: File path empty ", daily_log_file)
            print("File path cannot be empty. Please enter a valid file path.")


def submenu_create_event_flat():
    """
    Method: submenu_create_event_flat
    Purpose: displays the submenu for creating an event from a flat file.
    """
    utils.write_to_daily_log_file("Create event from flat file function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    print("Enter the file path:")
    file_name = input("File path: ")
    while True:
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Create event from flat file function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            try:
                datafile = "data/out/users.json"
                event_service_instance = event_service.EventServices()
                event_service_instance.create_event_flat(file_name, logged_in_user.username,
                                                         sys_users, datafile)
                utils.write_to_daily_log_file("Create event from flat file function: Event created successfully " +
                                              str(logged_in_user), daily_log_file)
                main_menu()
                break
            except Exception as e:
                utils.write_to_daily_log_file("Create event from flat file function: Error " + str(e), daily_log_file)
                print("Error: ", e)
                main_menu()
                break
        elif choice == "2":
            utils.write_to_daily_log_file("Create event from flat file function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            submenu_create_event_category()
            break
        else:
            utils.write_to_daily_log_file("Create event from flat file function: User " + str(logged_in_user) +
                                          "Choice: " + str(choice), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_view_event():
    """
    Method: submenu_view_event
    Purpose: displays the submenu for viewing an event.
    """
    utils.write_to_daily_log_file("View event function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    print("How would you like to view the event?")
    print("1. View all my events")
    print("2. View a specific event")
    print("3. Return to main menu")
    print("4. Logout")
    choice = input("Enter your choice: ")
    while True:
        utils.write_to_daily_log_file("View event function: Choice " + choice, daily_log_file)
        event_service_instance = event_service.EventServices()

        if choice == "1":
            utils.write_to_daily_log_file("View event function: View all my events - User" +
                                          str(logged_in_user) + "Choice" + str(choice), daily_log_file)

            event_service_instance.get_all_events(
                logged_in_user.username, sys_users)
            main_menu()
            break
        elif choice == "2":
            utils.write_to_daily_log_file("View event function: View a specific event - User" +
                                          str(logged_in_user) + "Choice" + str(choice), daily_log_file)
            submenu_view_specific_event()
            break
        elif choice == "3":
            utils.write_to_daily_log_file("View event function: Return to main menu - User" +
                                          str(logged_in_user) + "Choice" + str(choice), daily_log_file)
            main_menu()
            break
        elif choice == "4":
            utils.write_to_daily_log_file("View event function: Logout - User" +
                                          str(logged_in_user) + "Choice" + str(choice), daily_log_file)
            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("View event function: Invalid choice - User" +
                                          str(logged_in_user) + "Choice" + str(choice), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_view_specific_event():
    """
    Method: submenu_view_specific_event
    Purpose: displays the submenu for viewing a specific event.
    :return:
    """
    utils.write_to_daily_log_file("View specific event function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    event_service_instance = event_service.EventServices()
    print("Enter the event title:")
    title = input("Title: ")
    event_exists = event_service_instance.check_event_exists(title, logged_in_user.username, sys_users)
    if not event_exists:
        utils.write_to_daily_log_file("View specific event function: User " + str(logged_in_user) +
                                      "Event " + title + " does not exist", daily_log_file)
        print("Event does not exist!")
        main_menu()
    while True:
        utils.write_to_daily_log_file("View specific event function: Title " + title, daily_log_file)
        print("Are you sure you want to view the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("View specific event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            event_service_instance.get_event(
                title, logged_in_user.username, sys_users)
            main_menu()
            break
        elif choice == "2":
            utils.write_to_daily_log_file("View specific event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            main_menu()
            break
        else:
            utils.write_to_daily_log_file("View specific event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_update_event():
    """
    Method: submenu_update_event
    Purpose: displays the submenu for updating an event.
    """
    utils.write_to_daily_log_file("Update event function: CALL ", daily_log_file)
    event_service_instance = event_service.EventServices()
    global logged_in_user
    global sys_users
    datafile = "data/out/users.json"
    print("Enter the event title: ")
    old_title = input("Title: ")
    event_exists = event_service_instance.check_event_exists(
        old_title, logged_in_user.username, sys_users)
    if not event_exists:
        utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                      "Event " + old_title + " does not exist", daily_log_file)
        print("Event does not exist!")
        main_menu()


    print("Enter the updated event details:")
    title = input("New Title: ")
    date = input("New Date: (yyyy-mm-dd)")
    description = input("New Description: ")

    while True:
        utils.write_to_daily_log_file("Update event function: Title " + title + ", Date " + date +
                                          ", Description " + description, daily_log_file)
        print("Are you sure you want to update the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            try:
                event_service_instance.update_event(
                    old_title, title, date, description, logged_in_user.username, sys_users, datafile)
                utils.write_to_daily_log_file("Update event function: Event updated successfully ", daily_log_file)
                main_menu()
            except Exception as e:
                utils.write_to_daily_log_file("Update event function: Error " + str(e), daily_log_file)
                print("Error: ", e)
                break
        elif choice == "2":
            utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            main_menu()
            break
        else:
            utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                          "Choice " + str(choice), daily_log_file)
            print("Invalid choice! Please try again.")


def submenu_delete_event():
    """
    Method: submenu_delete_event
    Purpose: displays the submenu for deleting an event.
    """
    utils.write_to_daily_log_file(
        "Delete event function: CALL ", daily_log_file
    )
    global logged_in_user
    global sys_users
    event_service_instance = event_service.EventServices()
    datafile = "data/out/users.json"
    print("Enter the event title:")
    title = input("Title: ")
    event_exists = event_service_instance.check_event_exists(
        title, logged_in_user.username, sys_users)
    if not event_exists:
        utils.write_to_daily_log_file(
            "Delete event function: User " + str(logged_in_user) +
            "Event " + title + " does not exist", daily_log_file
        )
        print("Event does not exist!")
        main_menu()
    while True:
        utils.write_to_daily_log_file(
            "Delete event function: Title " + title, daily_log_file
        )
        print("Are you sure you want to delete the event?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file(
                    "Delete event function: Choice " + choice, daily_log_file
            )
            try:
                event_service_instance.delete_event(title, logged_in_user.username, sys_users, datafile)
                utils.write_to_daily_log_file(
                    "Delete event function: Event deleted successfully ", daily_log_file
                )
                main_menu()
            except Exception as e:
                utils.write_to_daily_log_file(
                    "Delete event function: Error " + str(e), daily_log_file
                )
                print("Error: ", e)
                break
        elif choice == "2":
            utils.write_to_daily_log_file(
                "Delete event function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            main_menu()
            break
        else:
            utils.write_to_daily_log_file(
                "Delete event function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            print("Invalid choice! Please try again.")


def submenu_logout():
    """
    Method: submenu_logout
    Purpose: displays the submenu for logging out.
    """
    utils.write_to_daily_log_file(
        "Logout function: CALL ", daily_log_file
    )
    global logged_in_user
    global sys_users
    if logged_in_user is None:
        utils.write_to_daily_log_file(
            "Logout function: No user is currently logged in", daily_log_file
        )
        print("No user is currently logged in.")
        return

    print(
        "Are you sure you want to logout from [", logged_in_user.username, "]?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    while True:
        if choice == "1":
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            try:
                user_service.UserService().logout_user(sys_users, logged_in_user.username)
                print("User logged out successfully!")
                utils.write_to_daily_log_file(
                    "Logout function: User logged out successfully ", daily_log_file
                )
                logged_in_user = None
                auth_menu()
            except Exception as e:
                utils.write_to_daily_log_file(
                    "Logout function: Error " + str(e), daily_log_file
                )
                print("Error: ", e)
                break
        elif choice == "2":
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            main_menu()
            break
        else:
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
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
        utils.create_log_file_if_not_exists()
        auth_menu()
        pass
