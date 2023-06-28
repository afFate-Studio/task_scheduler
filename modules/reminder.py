import datetime
import time
import pyinputplus as pyip
import schedule
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your Google service account credentials JSON file
SERVICE_ACCOUNT_FILE = '../credentials.json'

# ID of the Google Calendar where you want to create reminders
CALENDAR_ID = 'your-calendar-id@example.com'

def send_reminder(task):
    # Modify this function according to your preferred method of sending reminders
    create_calendar_reminder(task, datetime.datetime.now() + datetime.timedelta(minutes=1))

def create_calendar_reminder(task, reminder_time):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': task,
        'start': {'dateTime': reminder_time.isoformat()},
        'end': {'dateTime': reminder_time.isoformat()},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 1},
            ],
        },
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

class Reminder():
    def __init__(self, task, weeks, days, hours, minutes, seconds):
        self.task = task["name"]
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.scheduled_job = None

        if self.weeks:
            self.scheduled_job = schedule.every(self.weeks).weeks.do(self.send_reminder_wrapper)
        elif self.days:
            self.scheduled_job = schedule.every(self.days).days.do(self.send_reminder_wrapper)
        elif self.hours:
            self.scheduled_job = schedule.every(self.hours).hours.do(self.send_reminder_wrapper)
        elif self.minutes:
            self.scheduled_job = schedule.every(self.minutes).minutes.do(self.send_reminder_wrapper)
        elif self.seconds:
            self.scheduled_job = schedule.every(self.seconds).seconds.do(self.send_reminder_wrapper)

        self.run_schedule_loop()

    def send_reminder_wrapper(self):
        send_reminder(self.task)
        if self.scheduled_job is not None:
            self.scheduled_job.cancel()

    def send_reminder(self, task):
        send_reminder(task)

    def run_schedule_loop(self):
        while True:
            schedule.run_pending()
            time.sleep(1)