#import notify2
import pyinputplus as pyip
import os
import schedule
import time

# DOCS for schedule module
# https://schedule.readthedocs.io/en/stable/
class Reminder():
    def __init__(self, task):
        self.task = task
        self.weeks = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def job(self):
        print("test")

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

    # function used to get reminder info from user, in order to set a reminder for a task
    def get_reminder_time(self):
            print("\tWeeks -> Days -> Hours:Minutes:Seconds")
            self.weeks = pyip.inputNum("In how many weeks would you like to be reminded : ", min = 0, max = 51)
            self.days = pyip.inputNum("In how many days would you like to be reminded : ", min = 0, max = 6)
            reminder_time = pyip.inputTime("How often would you like to be reminded, max value is 23:59:59 : ", formats = ("%H:%M:%S", "%H:%M", "%X"))
            self.hours = int(reminder_time.hour) 
            self.minutes = int(reminder_time.minute)
            self.seconds = int(reminder_time.second)
    