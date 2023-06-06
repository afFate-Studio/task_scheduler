#import notify2
import os
import schedule
import time

# DOCS for schedule module
# https://schedule.readthedocs.io/en/stable/

class Reminder:

    def __init__(self, task, weeks, days, hours, minutes, seconds):
        self.task = task
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

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

    