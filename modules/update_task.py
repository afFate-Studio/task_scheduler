import pyinputplus as pyip
from modules.get_response import *
from modules.reminder import *

def updater(task, name, complete, remind, priority, comment):
    task['name'] = name
    task['completed'] = complete
    task['reminder'] = remind
    task['priority'] = priority
    task['comments'] = comment
    

def update_task(tasks):
    print('Please select a task you would like to edit based on it\'s name: ')
    for dict, info in enumerate(tasks):
        print(tasks[info]['name'])
    user_task = pyip.inputStr('Which task would you like to update: ')


    for dict, info in enumerate(tasks):
        if user_task == tasks[info]['name']:
            new_name_response = ask_user('Would you like to enter a new name for this task: ( Y | N ): ')
            new_completion_status = ask_user('Would you like to change the completion status of this task ( Y | N ): ')
            new_reminder_status = ask_user('Would you like to update the reminder status of this task ( Y | N ): ')
            new_priority = ask_user('Would you like to change the priority of this task ( Y | N ): ')
            new_comment = ask_user('Would you like to update the comment for this task (previous comment will be overwritten) ( Y | N ): ')
            
            if new_name_response == 'Y':
                while True:
                    try:
                        task_name = pyip.inputStr("\nEnter the new task name: ") # get task name from user

                        for dict, info in enumerate(tasks):
                            if task_name == tasks[info]['name']:
                                raise ValueError('Task name already taken')
                        break
                    except ValueError:
                        print('Task name already taken')
            else:
                task_name = task[info]['name']

            if new_completion_status == 'Y':
                completed = ask_user('Is your task completed ( Y | N ): ')
            else:
                completed = tasks[info]['completed']

            if new_reminder_status == 'Y':
                task_reminder_status = ask_user("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
                if task_reminder_status == 'Y':    # check response for a positive response
                    reminder_info = get_reminder_time()
                    Reminder(task=tasks[info], weeks=reminder_info[0], days=reminder_info[1], \
                             hours=reminder_info[2], minutes=reminder_info[3], seconds=reminder_info[4]).job(tasks_dict=tasks[info])
            else:
                task_reminder_status = tasks[info]['reminder']

            if new_priority == 'Y':
                # Checks response for task_priority, appends the result if correct, otherwise prompts user for correct response
                while True:
                    try:
                        task_priority = pyip.inputNum("Enter the priority of this task ( 0 - 10 ): ") # get task priority from the user
                        if task_priority not in range(11):
                            raise ValueError
                        else: break
                    except ValueError: 
                        print("Oops! That was not a valid choice, please try again.")
            else:
                task_priority = task[info]['priority']
            if new_comment == 'Y':
                comment = pyip.inputStr('Enter the new comment for the task: ')
            else:
                comment = tasks[info]['comments']

    
            updater(task=tasks[info], name=task_name, complete=completed, remind=task_reminder_status, priority=task_priority, comment=comment)

    return tasks