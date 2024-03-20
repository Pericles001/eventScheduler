"""
File: event_scheduler_ui.py
Class: EventSchedulerUI
Purpose: contains the user interface for the event scheduler application.
"""
import src.service.event_services as event_service
import src.service.users_service as user_service
import src.utils.utils as utils

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
    if utils.is_empty(username):
        print("Username cannot be empty. Please enter a valid username.")
        register_user()
    password = input("Password: ")
    if utils.is_empty(password):
        print("Password cannot be empty. Please enter a valid password.")
        register_user()
    email = input("Email: ")
    if utils.is_empty(email):
        print("Email cannot be empty. Please enter a valid email.")
        register_user()
    full_name = input("Full Name: ")
    if utils.is_empty(full_name):
        print("Full Name cannot be empty. Please enter a valid full name.")
        register_user()
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
                print("User created successfully! Login to continue.")
                auth_menu()
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
            register_user()


def login_user():
    """
    Method: login_user
    Purpose: displays the login form.
    """
    utils.write_to_daily_log_file("User login function: CALL ", daily_log_file)
    global logged_in_user  # To modify the global variable
    print("Enter the user details:")
    username = input("Username: ")
    if utils.is_empty(username):
        print("Username cannot be empty. Please enter a valid username.")
        login_user()
    password = input("Password: ")
    if utils.is_empty(password):
        print("Password cannot be empty. Please enter a valid password.")
        login_user()
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
            else:
                utils.write_to_daily_log_file("User login function: User login failed ", daily_log_file)
                auth_menu()
            break
        elif choice == "2":
            utils.write_to_daily_log_file("User login function: User login cancelled ", daily_log_file)
            main_menu()
        else:
            print("Invalid choice! Please try again.")
            utils.write_to_daily_log_file("User login function: Invalid choice ", daily_log_file)
            login_user()
    return logged_in_user


def submenu_update_account():
    """
    Method: submenu_update_account
    Purpose: displays the submenu for updating the user account.
    :return:
    """
    global logged_in_user
    global sys_users
    user_service_instance = user_service.UserService()
    datafile = "data/out/users.json"
    utils.write_to_daily_log_file("Update account function: CALL ", daily_log_file)
    print("Enter the updated user details:")
    username = logged_in_user.username
    new_username = input("New Username:")
    if utils.is_empty(new_username):
        print("Username cannot be empty. Please enter a valid username.")
        submenu_update_account()
    password = input("New Password:")
    if utils.is_empty(password):
        print("Password cannot be empty. Please enter a valid password.")
        submenu_update_account()
    email = input("New Email:")
    if utils.is_empty(email):
        print("Email cannot be empty. Please enter a valid email.")
        submenu_update_account()
    full_name = input("New Full Name:")
    if utils.is_empty(full_name):
        print("Full Name cannot be empty. Please enter a valid full name.")
        submenu_update_account()
    utils.write_to_daily_log_file("Update account function: Username " + username, daily_log_file)
    while True:
        print("Are you sure you want to update your account?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        utils.write_to_daily_log_file("Update account function: CHOICE " + choice, daily_log_file)
        if choice == "1":
            encrypted_password = utils.encrypt_password(password)
            try:
                user_data = {
                    "username": new_username,
                    "password": encrypted_password,
                    "email": email,
                    "full_name": full_name,
                    "status": 0,
                    "events": logged_in_user.events
                }
                user_service_instance.update_user(logged_in_user.username, user_data, sys_users, datafile)
                utils.write_to_daily_log_file("Update account function: User updated successfully ", daily_log_file)
                print("Login with your new details.")
                auth_menu()
                break
            except Exception as e:
                print("Error: ", e)
                utils.write_to_daily_log_file("Update account function: Error " + str(e), daily_log_file)
                main_menu()
                break
        elif choice == "2":
            utils.write_to_daily_log_file("Update account function: User update cancelled ", daily_log_file)
            main_menu()
            break
        else:
            print("Invalid choice! Please try again.")
            utils.write_to_daily_log_file("Update account function: Invalid choice ", daily_log_file)
            submenu_update_account()


def submenu_delete_account():
    """
    Method: submenu_delete_account
    Purpose: displays the submenu for deleting the user account.
    """
    global logged_in_user
    global sys_users
    user_service_instance = user_service.UserService()
    datafile = "data/out/users.json"
    utils.write_to_daily_log_file("Delete account function: CALL ", daily_log_file)
    while True:
        print("Are you sure you want to delete your account?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        utils.write_to_daily_log_file("Delete account function: CHOICE " + choice, daily_log_file)
        if choice == "1":
            try:
                user_service_instance.delete_user(logged_in_user.username, sys_users, datafile)
                utils.write_to_daily_log_file("Delete account function: User deleted successfully ", daily_log_file)
                auth_menu()
                break
            except Exception as e:
                print("Error: ", e)
                utils.write_to_daily_log_file("Delete account function: Error " + str(e), daily_log_file)
                auth_menu()
                break


def submenu_manage_account():
    """
    Method: submenu_manage_account
    Purpose: displays the sub-menu for managing the user account.
    """
    utils.write_to_daily_log_file("Submenu manage account function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    sys_users = user_service.UserService().load_users()
    user_service_instance = user_service.UserService()
    print("======================================================================================================")
    print("1. View my account details")
    print("2. Update my account details")
    print("3. Delete my account")
    print("4. Return to main menu")
    print("5. Logout")
    print("======================================================================================================")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Submenu manage account function: View my account details - User" +
                                          str(logged_in_user), daily_log_file)
            user_service_instance.get_user_details(logged_in_user.username, sys_users)
            return_to_main_menu()
            break
        elif choice == "2":
            utils.write_to_daily_log_file("Submenu manage account function: Update my account details - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_update_account()
            return
        elif choice == "3":
            utils.write_to_daily_log_file("Submenu manage account function: Delete my account - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_delete_account()
            return
        elif choice == "4":
            utils.write_to_daily_log_file("Submenu manage account function: Return to main menu - User" +
                                          str(logged_in_user), daily_log_file)
            return_to_main_menu()
            break
        elif choice == "5":
            utils.write_to_daily_log_file("Submenu manage account function: Logout - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_logout()
            break
        else:
            print("Invalid choice! Please try again.")
            utils.write_to_daily_log_file("Submenu manage account function: Invalid choice - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_manage_account()


def main_menu():
    """
    Method: main_menu
    Purpose: displays the main menu.
    """
    utils.write_to_daily_log_file("Main menu function: CALL ", daily_log_file)
    global logged_in_user  # To access the global variable
    print("======================================================================================================")
    print("Welcome back, ", logged_in_user.username, "!", "It is:", utils.get_current_time())
    print("0. Manage Account")
    print("1. Create Event")
    print("2. View Event")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Logout")
    print("======================================================================================================")
    while True:
        choice = input("Enter your choice: ")
        if choice == "0":
            utils.write_to_daily_log_file("Main menu function: Manage account ", daily_log_file)
            submenu_manage_account()
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
            main_menu()


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
            return_to_main_menu()


def auth_menu():
    """
    Method: auth_menu
    Purpose: displays the authentication menu.
    """
    utils.write_to_daily_log_file("Authentication menu function: CALL ", daily_log_file)
    print("======================================================================================================")
    print("Welcome to the Event Scheduler!")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("======================================================================================================")
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
            auth_menu()


def submenu_create_event_category():
    """
    Method: submenu_create_event_category
    """
    utils.write_to_daily_log_file("Create event category function: CALL ", daily_log_file)
    print("======================================================================================================")
    print("1. Import Event details from a file")
    print("2. Enter Event details manually")
    print("3. Return to main menu")
    print("4. Logout")
    print("======================================================================================================")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file("Create event category function: Import event details from a file - User:" +
                                          str(logged_in_user), daily_log_file)
            submenu_create_event_file()
            return  # Add return statement after calling submenu function
        elif choice == "2":
            utils.write_to_daily_log_file("Create event category function: Enter event details manually - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_create_event_manual()
            return  # Add return statement after calling submenu function
        elif choice == "3":
            utils.write_to_daily_log_file("Create event category function: Return to main menu - User" +
                                          str(logged_in_user), daily_log_file)
            return_to_main_menu()
            return  # Add return statement after calling submenu function
        elif choice == "4":
            utils.write_to_daily_log_file("Create event category function: Logout - User" +
                                          str(logged_in_user), daily_log_file)
            submenu_logout()
            break
        else:
            utils.write_to_daily_log_file("Create event category function: Invalid choice - User" +
                                          str(logged_in_user), daily_log_file)
            print("Invalid choice! Please try again.")
            submenu_create_event_category()
        break


def submenu_create_event_manual():
    """
    Method: submenu_create_event_manual
    Purpose: displays the submenu for creating an event manually.
    """
    utils.write_to_daily_log_file("Create event manually function: CALL ", daily_log_file)
    print("Enter the event details:")
    title = input("Title: ")
    if utils.is_empty(title):
        print("Title cannot be empty. Please enter a valid title.")
        submenu_create_event_manual()
    date = input("Date: (yyyy-mm-dd)")
    if utils.is_empty(date):
        print("Date cannot be empty. Please enter a valid date.")
        submenu_create_event_manual()
    elif not utils.is_valid_date(date):
        print("Invalid date format. Please enter a valid date in the format yyyy-mm-dd.")
        submenu_create_event_manual()
    description = input("Description: ")
    if utils.is_empty(description):
        print("Description cannot be empty. Please enter a valid description.")
        submenu_create_event_manual()
    while True:
        utils.write_to_daily_log_file("Create event manually function: User " + str(logged_in_user) + "Details: " +
                                      str(title) + ", " + str(date) + ", "
                                      + str(description), daily_log_file)
        print("======================================================================================================")
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        print("======================================================================================================")
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
            submenu_create_event_manual()


def submenu_create_event_file():
    """
    Method: submenu_create_event_file
    Purpose: displays the submenu for creating an event from a file.
    """
    utils.write_to_daily_log_file("Create event from file function: CALL ", daily_log_file)
    print("======================================================================================================")
    print("1. Import the event details from a json file:")
    print("2. Import the event details from a flat file:")
    print("3. Return to main menu")
    print("4. Logout")
    print("======================================================================================================")
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
            submenu_create_event_file()


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
            print(
                "======================================================================================================")
            print("Are you sure you want to create the event?")
            print("1. Yes")
            print("2. No")
            print(
                "======================================================================================================")
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
                submenu_create_event_json()
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
        print("======================================================================================================")
        print("Are you sure you want to create the event?")
        print("1. Yes")
        print("2. No")
        print("======================================================================================================")
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
            submenu_create_event_flat()


def submenu_view_event():
    """
    Method: submenu_view_event
    Purpose: displays the submenu for viewing an event.
    """
    utils.write_to_daily_log_file("View event function: CALL ", daily_log_file)
    global logged_in_user
    global sys_users
    while True:
        print("======================================================================================================")
        print("How would you like to view the event?")
        print("1. View all my events")
        print("2. View a specific event")
        print("3. Return to main menu")
        print("4. Logout")
        print("======================================================================================================")
        choice = input("Enter your choice: ")
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
        print("======================================================================================================")
        print("Are you sure you want to view the event?")
        print("1. Yes")
        print("2. No")
        print("======================================================================================================")
        choice = input("Enter your choice: ")
        utils.write_to_daily_log_file("View specific event function: Title " + title, daily_log_file)
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
    # check if the title is empty
    if utils.is_empty(title):
        utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                      "Title " + title + " is empty", daily_log_file)
        print("Title cannot be empty! Please try again.")
        submenu_update_event()
    date = input("New Date: (yyyy-mm-dd)")
    # check if the date is valid
    if not utils.is_valid_date(date):
        utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                      "Invalid date " + date, daily_log_file)
        print("Invalid date!Try again with the correct date format (yyyy-mm-dd)")
        submenu_update_event()
    description = input("New Description: ")
    # check if the description is empty
    if utils.is_empty(description):
        utils.write_to_daily_log_file("Update event function: User " + str(logged_in_user) +
                                      "Description " + description + " is empty", daily_log_file)
        print("Description cannot be empty! Please try again.")
        submenu_update_event()

    while True:
        utils.write_to_daily_log_file("Update event function: Title " + title + ", Date " + date +
                                      ", Description " + description, daily_log_file)
        print("======================================================================================================")
        print("Are you sure you want to update the event?")
        print("1. Yes")
        print("2. No")
        print("======================================================================================================")
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
            submenu_update_event()


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
        print("======================================================================================================")
        print("Are you sure you want to delete the event?")
        print("1. Yes")
        print("2. No")
        print("======================================================================================================")
        choice = input("Enter your choice: ")
        if choice == "1":
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
            submenu_delete_event()


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
        auth_menu()
    print("======================================================================================================")
    print(
        "Are you sure you want to logout from [", logged_in_user.username, "]?")
    print("1. Yes")
    print("2. No")
    print("======================================================================================================")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            try:
                utils.write_to_daily_log_file("User details loaded successfully!" + "\n", daily_log_file)
                user_service.UserService().logout_user(sys_users, logged_in_user.username)
                print("User logged out successfully!")
                utils.write_to_daily_log_file(
                    "Logout function: User logged out successfully ", daily_log_file
                )
                logged_in_user = None
                auth_menu()
                break  # Exit the loop after successful logout
            except Exception as e:
                utils.write_to_daily_log_file(
                    "Logout function: Error " + str(e), daily_log_file
                )
                print("Error: ", e)
                break  # Exit the loop if an error occurs
        elif choice == "2":
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            main_menu()
            break  # Exit the loop if the user chooses not to logout
        else:
            utils.write_to_daily_log_file(
                "Logout function: User " + str(logged_in_user) +
                "Choice " + str(choice), daily_log_file
            )
            print("Invalid choice! Please try again.")
            submenu_logout()


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
        auth_menu()
        pass
