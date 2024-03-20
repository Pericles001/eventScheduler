#!/usr/bin/python3
"""
File: event_services.py
Class: EventServices - contains the services for the event object  (operations on the event object).
"""
import json

import python.src.io.flat_builder
import python.src.io.json_builder
import python.src.model.event as event
import python.src.repository.repository as repo


class EventServices:
    """
    Class: EventServices
    Purpose: contains the services for the event object  (operations on the event object).
    """

    def __init__(self):
        self.repo = repo.EventRepository()

    def create_event(self, title, date, description, event_owner, sys_users, datafile):
        """
        Create a new event.

        Args:
            title (string): The title of the event.
            date (datetime [yyyy-mm-dd]): represents the date of the event in the format yyyy-mm-dd.
            description (string): description of the event.
        :param title:
        :param date:
        :param description:
        :return:
        """
        owner_name = event_owner
        try:
            new_event = event.Event(title, date, description)
            self.repo.add_event(new_event)
            for username, user_data in sys_users.items():
                if username == owner_name:
                    print("Event: ", new_event.title, " ",
                          new_event.date, " ", new_event.description)
                    # Append the event details to the corresponding user's events list
                    convert_date = str(new_event.date.strftime('%Y-%m-%d'))
                    print("Event date: ", convert_date)
                    user_data["events"].append(
                        {"title": new_event.title, "date": convert_date, "description": new_event.description})
                    print("Event added to events list")

                    with open(datafile, 'w') as f:
                        json.dump(sys_users, f, indent=4)
                        print("Data saved to file")
                    break
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_all_events(self, events_owner, sys_users):
        """
        Get all events from the repository.
        """
        owner_name = events_owner
        try:
            for username, user_data in sys_users.items():
                if username == owner_name:
                    #             display events in a table like format
                    print("Events: ", user_data["events"], "\n")
                    for event in user_data["events"]:
                        print("Title: ", event["title"])
                        print("Date: ", event["date"])
                        print("Description: ", event["description"])
                        print("\n")
                    return user_data["events"]
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_event(self, title, events_owner, sys_users):
        """
        Get an event from the repository.

        Args:
            title (string): The name of the event to get.
        """
        owner_name = events_owner

        try:
            for username, user_data in sys_users.items():
                if username == owner_name:
                    for event in user_data["events"]:
                        if event["title"] == title:
                            # print the event details
                            print("Title: ", event["title"])
                            print("Date: ", event["date"])
                            print("Description: ", event["description"])
                            print("\n")
                            return event

                    print("Event not found")
                    return None
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_event_string(self, title):
        """
        Get an event from the repository.

        Args:
            title (string): The name of the event to get.
        """
        try:
            target_event = self.repo.get_event(title)
            return "Title: " + target_event.title + "\nDate: " + target_event.date + "\nDescription: " + target_event.description
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
            return None

    def get_all_events_string(self):
        """
        Get all events from the repository.
        """
        try:
            events = self.repo.get_all_events()
            result = ""
            for event in events:
                result += "Title: " + event.title + "\nDate: " + \
                          event.date + "\nDescription: " + event.description + "\n\n"
            return result
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
            return None

    def check_event_exists(self, title, events_owner, sys_users):
        """
        Check if an event exists in the repository.

        Args:
            title (string): The name of the event to check.
        """
        owner_name = events_owner
        try:
            for username, user_data in sys_users.items():
                if username == owner_name:
                    for event in user_data["events"]:
                        if event["title"] == title:
                            print("Event found: [", title, "]")
                            return True
                    print("Event not found")
                    return False  # Return False after checking all events
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def update_event(self, title, new_title, new_date, new_description, event_owner, sys_users, datafile):
        """
        Update an event in the repository.

        Args:
            title (string): The name of the event to update.
            new_title (string): The new title of the event.
            new_date (datetime [yyyy-mm-dd]): represents the new date of the event in the format yyyy-mm-dd.
            new_description (string): new description of the event.
        """
        owner_name = event_owner
        print("Owner name", owner_name)
        try:
            #  check if the event exists first
            for username, user_data in sys_users.items():
                if username == owner_name:
                    for event in user_data["events"]:
                        if event["title"] == title:
                            print("Event found: [", title, "]")
                            # update the event details
                            event["title"] = new_title
                            event["date"] = new_date
                            event["description"] = new_description
                            print("Event updated: [", new_title, "]")

                            # Write the updated data to the database file
                            with open(datafile, 'w') as f:
                                json.dump(sys_users, f, indent=4)
                                print("Data written to file")
                                break

        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def delete_event(self, title, events_owner, sys_users, datafile):
        """
        Delete an event from the repository.

        Args:
            title (string): The name of the event to delete.
        """
        owner_name = events_owner
        try:
            for username, user_data in sys_users.items():
                if username == owner_name:
                    for event in user_data["events"]:
                        if event["title"] == title:
                            print("Event found: [", title, "]")
                            # delete the event
                            user_data["events"].remove(event)
                            print("Event deleted: [", title, "]")

                            # Write the updated data to the database file
                            with open(datafile, 'w') as f:
                                json.dump(sys_users, f, indent=4)
                                print("Data written to file")
                                break
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def get_events_by_year(self, year):
        """
        Get all events from the repository for a given year.

        Args:
            year (int): The year to get the events for.
            :param self:
        """
        try:
            events = self.repo.get_all_events()
            result = []
            for event in events:
                if event.date.year == year:
                    result.append(event)
            return result
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

    def create_event_json(self, filepath, event_owner, sys_users, datafile):
        """
        Method: create_event_json
        Purpose: creates an event from a json file.
        """
        owner_name = event_owner
        try:
            json_builder = python.src.io.json_builder.JsonBuilder()
            event = json_builder.build_event(filepath)

            # Iterate over the items (key, value pairs) in sys_users
            for username, user_data in sys_users.items():
                if username == owner_name:
                    print("Event: ", event.title, " ",
                          event.date, " ", event.description)
                    # Append the event details to the corresponding user's events list
                    convert_date = str(event.date.strftime('%Y-%m-%d'))
                    print("Event date: ", convert_date)
                    user_data["events"].append(
                        {"title": event.title, "date": convert_date, "description": event.description})
                    print("Event added to events list")

                    # Write the updated data to the database file
                    with open(datafile, 'w') as f:
                        json.dump(sys_users, f, indent=4)
                        print("Data saved to file")
                        break  # Stop iterating once the user is found and event is added
        except FileNotFoundError as fnfe:
            print(fnfe)
        except json.JSONDecodeError as jde:
            print(jde)

    def create_event_flat(self, filepath, event_owner, sys_users, datafile):
        """
        Method: create_event_flat
        Purpose: creates an event from a flat file.
        """
        try:
            flat_builder = python.src.io.flat_builder.FlatBuilder()
            event = flat_builder.build_event(filepath)
            owner_name = event_owner
            # Iterate over the items (key, value pairs) in sys_users
            for username, user_data in sys_users.items():
                if username == owner_name:
                    print("Event: ", event.title, " ",
                          event.date, " ", event.description)
                    # Append the event details to the corresponding user's events list
                    convert_date = str(event.date.strftime('%Y-%m-%d'))
                    print("Event date: ", convert_date)
                    user_data["events"].append(
                        {"title": event.title, "date": convert_date, "description": event.description})
                    print("Event added to user list")

                    # Write the updated data to the database file
                    with open(datafile, 'w') as f:
                        json.dump(sys_users, f, indent=4)
                        print("Data written to file")
                        break  # Stop iterating once the user is found and event is added
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        finally:
            print("Event created from flat file")
