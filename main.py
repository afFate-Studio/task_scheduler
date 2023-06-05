# this program is used to keep track of tasks I need to complete
from tasks import Task
from emailer import Emailer
from load import File_Handling
import os

# function used to check the response from the user to make sure it is a valid response
def check_response(response):
    while True:
        try:
            for i in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
                if response == i:   # if valid response, ends loop and returns response
                    return response
            response = input("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response
        except ValueError:
            pass
        
# function used to check if user wants to email task list to themselves or other people
def email_list(task):
    sender_email = input("\nPlease provide the sender gmail address ( ex. sender@gmail.com ): ") # take the users email address
    app_password = input("Please provide your gmail app password: ")    # take the users gmail app password
    reciever_email = input("Please provide the recievers email address ( ex. reciever@mail.com ): ") # take the email they wish to send the task to
    Emailer(sender_email, app_password, reciever_email, task)   # pass the variables into the Emailer class


# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
    # empty list for task info
    task_info = []
      
    task_name = input("\nEnter the task name: ") # get task name from user
    task_info.append(task_name) # append task name to task_info list

    task_completion_status = input("Enter the task completion status ( Y | N ): ") # get task completion status from user
    checked_completion_status = check_response(task_completion_status)  # check for valid response
    task_info.append(checked_completion_status) # append response to task_info list

    task_reminder_status = input("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    checked_reminder_status = check_response(task_reminder_status)  # check for valid response
    task_info.append(checked_reminder_status)   # append response to task_info list

    # Checks response for task_priority, appends the result if correct, otherwise prompts user for correct response
    while True:
        try:
            task_priority = int(input("Enter the priority of this task ( 0, 1, 2, 3 ): ")) # get task priority from the user
            if task_priority in range(4):
                task_info.append(task_priority) # append the task priority to task_info list
                break
        except ValueError:
            print("Oops! That was not a valid choice, please try again.")

    task_comment = input ("Enter a comment for this task: ") # get task comment from user
    task_info.append(task_comment)  # append task comment to task_info list

    return task_info    # return task_info

# passes task_info list variables into the Task class, then returns the task object
def set_task(task_info):
    task = Task(task_info[0], task_info[1], task_info[2], int(task_info[3]), task_info[4]) # split task_info list into multiple variables and insert into Task class

    return task # return the task object

# error checking print function
"""
#def print_task(tasks):
#    print('\n')
#    for i in tasks:
#        print(i)
    """

def main():
    tasks = [] # empty list for task objects to be appended to

    response = input("Do you have a list file you would like to add to? ( Y | N ) : ")
    check_response(response)
    if response in ('Y','y','Yes','yes'):
        file_name = input("Please enter the full file path including the extension. ex. test.txt : ")
        while True:
            if os.path.exists(file_name):
                f = open(file_name, "r")
                f.read()
                break
            else:
                response = input("Invalid response would you like to try again ( Y | N ) : ")
                check_response(response)
                if response in ('Y','y','Yes','yes'):
                    file_name = input("Please enter the file path : ")
                else:
                    file_name = ""
                    break

    while True:

        task_info = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        task = set_task(task_info) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable

        tasks.append(task) # appending the task object with the user provided data

        # Ask user if they would like to add another task, if not ask if they would like to email the list
        response = input("\nWould you like to enter another task ( Y | N ): ")
        check_response(response) # check for valid response
        
        # checks user response to if they wish to continue, if yes loop will continue otherwise user will be asked if they would like to email their list
        # and loop will end
        if response in ('Y', 'y', 'Yes', 'yes'):
            continue
        else:
            response = input("\nWould you like to save your task list to a file ( Y | N ): ")
            if response in ('Y','y','Yes','yes'):
                if file_name == "":
                    file_name = input("Please enter a file name you would like: ")
                    f = File_Handling(file_name, tasks)
                    f.handling()
                else:
                    f = File_Handling(file_name, tasks)
                    f.handling()
            else:
                print("You chose to not save your task list to a file.")

            response = input("\nWould you like to email your task list ( Y | N ): ") # prompts user asking if they would like to email their task list
            check_response(response)    # checks user response
            if response in ('Y', 'y', 'Yes', 'yes'):
                email_list(task) # checks response and sends on doesn't send email based on the response
            else:
                print("Task list will not be emailed")   # if the user picks No, tell the user the list will not be emailed
                    

        
            break # break main loop
 

# TODO list of tasks, save user infomation on cloud or locale?, allow user to send task list to email or export as txt
if __name__ == '__main__':
    main()