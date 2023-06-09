# this program is used to keep track of tasks I need to complete
import pyinputplus as pyip                      # module to check user input
from modules.emailer import *                   # module to email a task list to an email provided by the user
from modules.reminder import *                  # module used to set reminders for tasks 
from modules.check_response import *            # module used to check the responses from the user
from modules.get_task_info import *             # module used to get the task information from the user
from modules.sorter import *                    # module used to sort the tasks_dict based on priority
from modules.tasks import *                     # module used to update the tasks_dict
from modules.get_response import *              # module used to ask user for a Y | N response
from modules.update_task import *               # module used to update tasks in the list based on user input
from modules.menu import *                      # module used as a menu for the user to select what they wish to do

def main():
    YES = 'Y'   # constant to check for a positive response

    file_name, tasks_dict = menu()      # calls the main menu

    # loops until user decides they have no more tasks to add
    while True:
        LENGTH = len(tasks_dict) # gets the length of tasks_dict
        task, reminder_info = get_task_info(tasks_dict=tasks_dict) # gets all tasks info (name, completion status, reminder, priority, comment) and reminder time then stores it into a variable 
        tasks_dict = Task(tasks_dict=tasks_dict, task=task) # updates tasks_dict with new tasks
        
        # Similar to LENGTH, not quite a constant but helps make logic less crowded
        REMINDER = tasks_dict["Task" + str(LENGTH)]["reminder"]
        # checks to see if the latest task appended into the dictionary wants a reminder then sets it if it does
        if REMINDER == YES:
            Reminder(task=tasks_dict["Task" + str(LENGTH)], weeks=reminder_info[0], days=reminder_info[1], \
                     hours=reminder_info[2], minutes=reminder_info[3], seconds=reminder_info[4]).send_reminder_wrapper()
        
        # takes tasks_dict, sorts it by the 'priority' key then returns the value
        sorted_tasks_dict = sort(tasks_dict=tasks_dict)

        """
            Asks user if they would like to continue adding more tasks,
            if yes the loop continues
            otherwise if the file wasn't provided by the user the user will be asked
            if they would like to save their file and be prompted to give a file name
            if they said yes.
            If file is provided the user will be asked if they would like to save to
            the provided file.
        """
        response = ask_user("\nWould you like to enter another task ( Y | N ): ")
        if response == YES:
            continue
        else:
            response = ask_user("Would you like to update any tasks in the list ( Y | N ): ")
            if response == YES:
                # takes the the sorted task list, allows user to update it, then resorts it
                sorted_tasks_dict = check_option(response=2, file_name=file_name, tasks_dict=sorted_tasks_dict)

            """
                User is asked if they would like to email their task list
                if yes, email will be sent.
            """
            response = ask_user("\nWould you like to email your task list ( Y | N ): ") # prompts user asking if they would like to email their task list
            if response == YES:
                Emailer(textfile=file_name) # checks response and sends on doesn't send email based on the response
                    
            save_file(file_name=file_name, sorted_tasks_dict=sorted_tasks_dict)

            break # break main loop

if __name__ == '__main__':
    main()
