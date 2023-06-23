import pyinputplus as pyip
from modules.check_response import *
from modules.reminder import *
from modules.set_task import *
from modules.get_response import *

# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
    # TODO check for duplicates, prevent the user from doing duplicates.
    # it will mess with the update_task functionality
    task_name = pyip.inputStr("\nEnter the task name: ") # get task name from user

    task_completion_status = ask_user("Enter the task completion status ( Y | N ): ") # get task completion status from user

    task_reminder_status = ask_user("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    if task_reminder_status == 'Y':    # check response for a positive response
        remind_time = get_reminder_time()

    # Checks response for task_priority, appends the result if correct, otherwise prompts user for correct response
    while True:
        try:
            task_priority = pyip.inputNum("Enter the priority of this task ( 0 - 10 ): ") # get task priority from the user
            if task_priority not in range(10):
                raise ValueError
            else: break
        except ValueError: 
            print("Oops! That was not a valid choice, please try again.")

    task_comment = pyip.inputStr("Enter a comment for this task: ") # get task comment from user

    task = set_task(task=task_name,completed=task_completion_status,reminder=task_reminder_status,priority=task_priority,comments=task_comment)
    if task_reminder_status == 'N':
        return task, None
    else:
        return task, remind_time
