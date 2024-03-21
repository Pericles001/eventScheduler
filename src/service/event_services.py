#!/usr/bin/python3
"""
File: event_services.py
Class: EventServices - contains the services for the event object  (operations on the event object).
"""
import json

import src.io.json_builder as json_builder
import src.io.flat_builder as flat_builder
import src.model.event as event
import src.repository.repository as repo

json_builder = json_builder.JsonBuilder()
flat_builder = flat_builder.FlatBuilder()


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
                        #     put the content as a list of dictionaries
                        json.dump(list(sys_users.values()), f, indent=4)
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
                    # sort the user events by date in ascending order before displaying
                    user_data["events"].sort(key=lambda x: x["date"])
                    print("Sorted events: ", user_data["events"], "\n")
                    for event in user_data["events"]:
                        print("Title: ", event["title"])
                        print("Date: ", event["date"])
                        print("Description: ", event["description"])
                        print("\n")
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
                                # json.dump(sys_users, f, indent=4)
                                json.dump(list(sys_users.values()), f, indent=4)
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
                                # json.dump(sys_users, f, indent=4)
                                json.dump(list(sys_users.values()), f, indent=4)
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
            # json_builder = src.io.json_builder.JsonBuilder()
            json_events = json_builder.build_event(filepath)

            # Iterate over the items (key, value pairs) in sys_users
            for username, user_data in sys_users.items():
                if username == owner_name:
                    if len(json_events) == 1:
                        user_data["events"].append(
                            {"title": json_events[0].title, "date": str(json_events[0].date.strftime('%Y-%m-%d')),
                             "description": json_events[0].description})
                        print("Event added to user list")
                    elif len(json_events) > 1:
                        for event_a in json_events:
                            print("Event: ", event_a.title, " ",
                                  event_a.date, " ", event_a.description)
                            # Append the event details to the corresponding user's events list
                            convert_date = str(event_a.date.strftime('%Y-%m-%d'))
                            print("Event date: ", convert_date)
                            user_data["events"].append(
                                {"title": event_a.title, "date": convert_date, "description": event_a.description})
                            print("Event added to events list")
                    elif len(json_events) == 0:
                        print("No events found in the file")
                        break

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
            # flat_builder = src.io.flat_builder.FlatBuilder()
            flat_events = flat_builder.build_event(filepath)
            owner_name = event_owner
            print("Length of flat events: ", len(flat_events))
            # Iterate over the items (key, value pairs) in sys_users
            for username, user_data in sys_users.items():
                if username == owner_name:
                    if len(flat_events) == 1:
                        user_data["events"].append(
                            {"title": flat_events[0].title, "date": str(flat_events[0].date.strftime('%Y-%m-%d')),
                             "description": flat_events[0].description})
                        print("Event added to user list")
                    elif len(flat_events) > 1:
                        for event_a in flat_events:
                            print("Event: ", event_a.title, " ",
                                  event_a.date, " ", event_a.description)
                            # Append the event details to the corresponding user's events list
                            convert_date = str(event_a.date.strftime('%Y-%m-%d'))
                            print("Event date: ", convert_date)
                            user_data["events"].append(
                                {"title": event_a.title, "date": convert_date, "description": event_a.description})
                            print("Event added to user list")
                    elif len(flat_events) == 0:
                        print("No events found in the file")
                        break

                    # Write the updated data to the database file
                    with open(datafile, 'w') as f:
                        json.dump(sys_users, f, indent=4)
                        print("Data written to file")
                        break  # Stop iterating once the user is found and event is added
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
