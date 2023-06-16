import pyinputplus as pyip

# function used to get reminder info from user, in order to set a reminder for a task
def get_reminder_time():
        print("\tWeeks -> Days -> Hours:Minutes:Seconds")
        weeks = pyip.inputNum("In how many weeks would you like to be reminded : ", min = 0, max = 51)
        days = pyip.inputNum("In how many days would you like to be reminded : ", min = 0, max = 6)
        reminder_time = pyip.inputTime("How often would you like to be reminded, max value is 23:59:59 : ", formats = ("%H:%M:%S", "%H:%M", "%X"))
        hours = int(reminder_time.hour) 
        minutes = int(reminder_time.minute)
        seconds = int(reminder_time.second)

        remind_time = [weeks, days, hours, minutes, seconds]

        return remind_time