import notify2
import os
import schedule
import time

# DOCS for schedule module
# https://schedule.readthedocs.io/en/stable/

class Reminder:

    def __init__(self, days, minutes, seconds, task):
        self.days = days
        self.minutes = minutes
        self.seconds = seconds
        self.task = task

    def job(self):
        pass

    def set_reminder(self):
        pass
    