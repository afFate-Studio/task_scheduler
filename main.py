# this program is used to keep track of tasks I need to complete
import pyinputplus as pyip              # module to check user input
from tasks import *                  # user made module to set task variables based on user input
from emailer import *             # user made module to email a task list to an email provided by the user
from file_handler import *  # user made module used to load and save to a file
from reminder import *
from check_response import *
from get_task_info import *
from set_task import *

def main():
    tasks = [] # empty list for task objects to be appended to

    # Prompt user for a file path
    response = pyip.inputStr("Do you have a list file you would like to add to? ( Y | N ) : ")
    response = check_response(response)
    if response in ('Y','y','Yes','yes'):
        file_name = pyip.inputFilepath("Please enter the full file path : ")
        f = File_Handling(file_name)    # tasks file path and sets the variable
        f.handling()    # checks if file exists, if it doesn't exists prompts user to make the file
    else:
        file_name = ""  # resets file_name to empty string

    while True:

        task_info = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        task = set_task(task_info) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable
        tasks.append(task) # appending the task object with the user provided data

        # TODO sort tasks based on priority

        # Ask user if they would like to add another task, if not ask if they would like to email the list
        response = pyip.inputStr("\nWould you like to enter another task ( Y | N ): ")
        response = check_response(response) # check for valid response
        
        # checks user response to if they wish to continue, if yes loop will continue otherwise user will be asked if they would like to email their list
        # and loop will end
        if response in ('Y', 'y', 'Yes', 'yes'):
            continue
        else:
            if file_name == "":
                response = pyip.inputStr("\nWould you like to save your task list to a file ( Y | N ): ")
                if response in ('Y','y','Yes','yes'):
                        file_name = pyip.inputFilepath("Please enter a file name you would like: ")
                        f = File_Handling(file_name, tasks)
                        f.saving()
                else:
                    print("You chose to not save your task list to a file.")
            else:
                f = File_Handling(file_name, tasks)
                f.saving()

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
