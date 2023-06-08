# this program is used to keep track of tasks I need to complete
import pyinputplus as pyip              # module to check user input
from tasks import *                     # module to set task variables based on user input
from emailer import *                   # module to email a task list to an email provided by the user
from file_handler import *              # module used to load and save to a file
from reminder import *                  # module used to set reminders for tasks 
from check_response import *            # module used to check the responses from the user
from get_task_info import *             # module used to get the task information from the user
from set_task import *                  # module used to set the task information

def main():
    tasks = [] # empty list for task objects to be appended to

    """
        Asks user if they have a list already made that they would like to add to
        Then checks the response to make sure it is a valid response
        Prompts user for the full file path depending on the users answer
        FileHandling checks the file path, if there is no file found it will prompt the user
        to choose either to create a new file or bypass the upload
    """
    response = pyip.inputStr("Do you have a list file you would like to add to? ( Y | N ) : ")
    response = check_response(response) # checks for valid response
    if response in ('Y','y','Yes','yes'):
        file_name = pyip.inputFilepath("Please enter the full file path : ")
        f = FileHandling(file_name)    # tasks file path and sets the variable
        f.handling()    # checks if file exists, if it doesn't exists prompts user to make the file
    else:
        file_name = ""  # resets file_name to empty string

    # loops until user decides they have no more tasks to add
    while True:

        task_info = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        task = set_task(task_info) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable
        tasks.append(task) # appending the task object with the user provided data

        # TODO sort tasks based on priority

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
        
        if response in ('Y', 'y', 'Yes', 'yes'):
            continue
        else:
            if file_name == "":
                response = pyip.inputStr("\nWould you like to save your task list to a file ( Y | N ): ")
                response = check_response(response)
                if response in ('Y','y','Yes','yes'):
                        file_name = pyip.inputFilepath("Please enter a file name you would like: ")
                        f = FileHandling(file_name, tasks)
                        f.saving()
                else:
                    print("You chose to not save your task list to a file.")
            else:
                response = pyip.inputStr("\nWould you like to save the new tasks to the file you provided? ( Y | N ): ")
                response = check_response(response)
                if response in ('Y','y','Yes','yes'):
                    f = FileHandling(file_name, tasks)
                    f.saving()
                else:
                    print("You chose not to save your tasks.")

            """
                User is asked if they would like to email their task list
                if yes, email will be sent.
            """
            response = pyip.inputStr("\nWould you like to email your task list ( Y | N ): ") # prompts user asking if they would like to email their task list
            response = check_response(response)    # checks user response
            if response in ('Y', 'y', 'Yes', 'yes'):
                Emailer(task) # checks response and sends on doesn't send email based on the response
            else:
                print("Task list will not be emailed")   # if the user picks No, tell the user the list will not be emailed
                
            break # break main loop

# TODO allow user to send task list to email or export as txt
if __name__ == '__main__':
    main()
