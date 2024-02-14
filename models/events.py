from models.event import *
import datetime

event1 = Event(datetime.date(2024, 2, 16), "Dinner with Mo", 8, False, 'SY8', "Bring a bottle")
event2 = Event(datetime.date(2024, 2, 14), "Research Github cert", 1, False, 'TW8', "Signup and begin training")
event3 = Event(datetime.date(2024, 2, 13), "Review Applications", 1, True, 'TW8', "Share with Andy and Alice")
event4 = Event(datetime.date(2024, 2, 15), "Register for AWS training", 1, False, 'TW8', "Review course options")

events = [event1, event2, event3, event4]

def add_new_event(event):
    events.append(event)

def delete_event(event_name):
    event_to_delete = None
    for event in events:
        if event.name == event_name:
            event_to_delete = event
            break

    events.remove(event_to_delete)

