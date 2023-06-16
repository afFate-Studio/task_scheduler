import pyinputplus as pyip
from check_response import *
from reminder import *
from tasks import *
from set_task import *

# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
      
    task_name = pyip.inputStr("\nEnter the task name: ") # get task name from user

    task_completion_status = pyip.inputStr("Enter the task completion status ( Y | N ): ") # get task completion status from user
    task_completion_status = check_response(task_completion_status)  # check for valid response

    task_reminder_status = pyip.inputStr("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    task_reminder_status = check_response(task_reminder_status)  # check for valid response
    if task_reminder_status == 'Y':    # check response for a positive response
        remind_time = get_reminder_time()

    # Checks response for task_priority, appends the result if correct, otherwise prompts user for correct response
    while True:
        try:
            task_priority = pyip.inputNum("Enter the priority of this task ( 0, 1, 2, 3 ): ") # get task priority from the user
            if task_priority not in range(4):
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
