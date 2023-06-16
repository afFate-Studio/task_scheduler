#import notify2
#import os
import time
import pyinputplus as pyip
import schedule
from modules.get_reminder_time import *

# DOCS for schedule module
# https://schedule.readthedocs.io/en/stable/
# TODO add threading 

#TODO reminders function - to actually send out a reminder 
# Might need to use something other than the schedule module
def set_reminder(self):
    schedule.every(self.weeks).weeks.do(self.job)
    schedule.every(self.days).days.do(self.job)
    schedule.every(self.hours).hours.do(self.job)
    schedule.every(self.minutes).minutes.do(self.job)
    schedule.every(self.seconds).seconds.do(self.job)

    while True:
        schedule.run_pending()
        time.sleep(1)


class Reminder():
    def __init__(self, task, weeks, days, hours, minutes, seconds):
        self.task = task["name"]
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        #set_reminder(self) # quite broken atm needs a lot of tweaking TODO

    # TODO make actual functionality now that it works
    def job(self, tasks_dict):
        print("Task: " + self.task)
        print("Completed: " + tasks_dict["completed"])
        print("Reminder: " + tasks_dict["reminder"])
        print("Priority: " + str(tasks_dict["priority"]))
        print("Comments: " + tasks_dict["comments"])
    