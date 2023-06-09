import pyinputplus as pyip
from check_response import *
from reminder import *

# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
    # empty list for task info
    task_info = []
    RESPONSES = ['Y','y','Yes','yes']
      
    task_name = pyip.inputStr("\nEnter the task name: ") # get task name from user
    task_info.append(task_name) # append task name to task_info list

    task_completion_status = pyip.inputStr("Enter the task completion status ( Y | N ): ") # get task completion status from user
    checked_completion_status = check_response(task_completion_status)  # check for valid response
    task_info.append(checked_completion_status) # append response to task_info list

    task_reminder_status = pyip.inputStr("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    checked_reminder_status = check_response(task_reminder_status)  # check for valid response
    task_info.append(checked_reminder_status)   # append response to task_info list
    for i in RESPONSES: # loop through responses
        if checked_reminder_status == i:    # check response against loop
            Reminder(task_name)   # get user variables for reminder information
            break

    # Checks response for task_priority, appends the result if correct, otherwise prompts user for correct response
    while True:
        try:
            task_priority = pyip.inputNum("Enter the priority of this task ( 0, 1, 2, 3 ): ") # get task priority from the user
            if task_priority in range(4):
                task_info.append(task_priority) # append the task priority to task_info list
                break
        except ValueError:
            print("Oops! That was not a valid choice, please try again.")

    task_comment = pyip.inputStr("Enter a comment for this task: ") # get task comment from user
    task_info.append(task_comment)  # append task comment to task_info list

    return task_info    # return task_info