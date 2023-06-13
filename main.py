# this program is used to keep track of tasks I need to complete
import pyinputplus as pyip              # module to check user input
from tasks import *                     # module to set task variables based on user input
from emailer import *                   # module to email a task list to an email provided by the user
from file_handler import *              # module used to load and save to a file
from reminder import *                  # module used to set reminders for tasks 
from check_response import *            # module used to check the responses from the user
from get_task_info import *             # module used to get the task information from the user
from set_task import *                  # module used to set the task information
from sorter import *                    # module used to sort the tasks_dict based on priority

def main():
    tasks_dict = {} # empty dictionary for task objects to be appended to
    YES = 'Y'   # constant to check for a positive response
    """
        Asks user if they have a list already made that they would like to add to
        Then checks the response to make sure it is a valid response
        Prompts user for the full file path depending on the users answer
        FileHandling checks the file path, if there is no file found it will prompt the user
        to choose either to create a new file or bypass the upload
    """
    response = pyip.inputStr("Do you have a list file you would like to add to? ( Y | N ) : ")
    response = check_response(response) # checks for valid response
    if response in YES:
        file_name = pyip.inputFilepath("Please enter the full file path : ")
        f = FileHandling(file_name)    # tasks file path and sets the variable
        f.handling()    # checks if file exists, if it doesn't exists prompts user to make the file
    else:
        file_name = ""  # resets file_name to empty string

    # loops until user decides they have no more tasks to add
    while True:

        task_info_list = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        if task_info_list[2] == YES:
            reminder_info = task_info_list.pop(3) # tasks the reminder info out of the task_info_list and makes it's own list
        task = set_task(task_info_list) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable
        
        LENGTH = len(tasks_dict) # Updated every loop with the list length, not exactly a constant
        

        # check the length of the dictionary and updates it according    
        if len(tasks_dict) == 0:
            tasks_dict.update({"Task0" : { "name" : task["name"],
                                           "completed" : task["completed"],
                                           "reminder" : task["reminder"],
                                           "priority" : task["priority"],
                                           "comments" : task["comments"]
                                           }})     
        else:
            
            tasks_dict.update({"Task" + str(LENGTH) : {"name" : task["name"],
                                                    "completed" : task["completed"],
                                                    "reminder" : task["reminder"],
                                                    "priority" : task["priority"],
                                                    "comments" : task["comments"]
                                                    }})
        
        # Similar to LENGTH, not quite a constant but helps make logic less crowded
        REMINDER = tasks_dict["Task" + str(LENGTH)]["reminder"]
        # checks to see if the latest task appended into the dictionary wants a reminder then sets it if it does
        if REMINDER == YES:
            Reminder(task=tasks_dict["Task" + str(LENGTH)], weeks=reminder_info[0], days=reminder_info[1], \
                     hours=reminder_info[2], minutes=reminder_info[3], seconds=reminder_info[4]).job(tasks_dict=tasks_dict["Task" + str(LENGTH)])
        
        # TODO sort tasks based on priority
        test_sort = sort(tasks_dict=tasks_dict, LENGTH=LENGTH)
        print(test_sort)

        
        """
            Asks user if they would like to continue adding more tasks,
            if yes the loop continues
            otherwise if the file wasn't provided by the user the user will be asked
            if they would like to save their file and be prompted to give a file name
            if they said yes.
            If file is provided the user will be asked if they would like to save to
            the provided file.
        """
        response = pyip.inputStr("\nWould you like to enter another task ( Y | N ): ")
        response = check_response(response) # check for valid response
        
        if response in YES:
            continue
        else:
            if file_name == "":
                response = pyip.inputStr("\nWould you like to save your task list to a file ( Y | N ): ")
                response = check_response(response)
                if response in YES:
                        file_name = pyip.inputFilepath("Please enter a file name you would like: ")
                        f = FileHandling(file_name, tasks_dict)
                        f.saving()
                else:
                    print("You chose to not save your task list to a file.")
            else:
                response = pyip.inputStr("\nWould you like to save the new tasks to the file you provided? ( Y | N ): ")
                response = check_response(response)
                if response in YES:
                    f = FileHandling(file_name, tasks_dict)
                    f.saving()
                else:
                    print("You chose not to save your tasks.")

            """
                User is asked if they would like to email their task list
                if yes, email will be sent.
            """
            response = pyip.inputStr("\nWould you like to email your task list ( Y | N ): ") # prompts user asking if they would like to email their task list
            response = check_response(response)    # checks user response
            if response in YES:
                Emailer(task) # checks response and sends on doesn't send email based on the response
            else:
                print("Task list will not be emailed")   # if the user picks No, tell the user the list will not be emailed
                
            break # break main loop

# TODO allow user to send task list to email or export as txt
if __name__ == '__main__':
    main()
