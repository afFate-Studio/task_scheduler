import datetime
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
import schedule

# Path to your Google service account credentials JSON file
SERVICE_ACCOUNT_FILE = '../credentials.json'

# ID of the Google Calendar where you want to create reminders
CALENDAR_ID = 'your-calendar-id@example.com'

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
        self.time_units = {
            'weeks': weeks,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
        self.scheduled_job = None
        self.schedule_job()

    def send_reminder_wrapper(self):
        self.send_reminder(self.task)

    def send_reminder(self, task):
        create_calendar_reminder(task, datetime.datetime.now() + datetime.timedelta(minutes=1))

    def schedule_job(self):
        for unit, value in self.time_units.items():
            if value:
                self.scheduled_job = getattr(schedule.every(value), unit).do(self.send_reminder_wrapper)
                break

        self.run_schedule_loop()

    def run_schedule_loop(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
