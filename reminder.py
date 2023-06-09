#import notify2
import pyinputplus as pyip
import os
import schedule
import time
from get_reminder_time import *

# DOCS for schedule module
# https://schedule.readthedocs.io/en/stable/
# TODO add threading 

class Reminder():
    def __init__(self, task):
        remind_time = get_reminder_time()
        self.task = task
        self.weeks = remind_time[0]
        self.days = remind_time[1]
        self.hours = remind_time[2]
        self.minutes = remind_time[3]
        self.seconds = remind_time[4]

    def job(self):
        for task in self.task:
            print("Task: " + task.task)
            print("Completed: " + task.completed)
            print("Reminder: " + task.reminder)
            print("Priority: " + str(task.priority))
            print("Comments: " + task.comments)
        print(str(self.weeks) + " " + str(self.seconds))

    #TODO reminders function - to actually send out a reminder 
    def set_reminder(self):
        schedule.every(self.weeks).weeks.do(self.job)
        schedule.every(self.days).days.do(self.job)
        schedule.every(self.hours).hours.do(self.job)
        schedule.every(self.minutes).minutes.do(self.job)
        schedule.every(self.seconds).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)

    