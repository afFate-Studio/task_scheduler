# this program is used to keep track of tasks I need to complete
import pyinputplus as pyip              # module to check user input
from tasks import Task                  # user made module to set task variables based on user input
from emailer import Emailer             # user made module to email a task list to an email provided by the user
from file_handler import File_Handling  # user made module used to load and save to a file

# function used to check the response from the user to make sure it is a valid response
def check_response(response):
    while True:
        try:
            for i in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
                if response == i:   # if valid response, ends loop and returns response
                    return response
            raise ValueError        
        except ValueError:
            response = input("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response
        
# function used to check if user wants to email task list to themselves or other people
def email_list(task):
    sender_email = pyip.inputEmail("\nPlease provide the sender gmail address ( ex. sender@gmail.com ): ") # take the users email address
    app_password = pyip.inputPassword("Please provide your gmail app password: ")    # take the users gmail app password
    reciever_email = pyip.inputEmail("Please provide the recievers email address ( ex. reciever@mail.com ): ") # take the email they wish to send the task to
    Emailer(sender_email, app_password, reciever_email, task)   # pass the variables into the Emailer class

# function used to get reminder info from user, in order to set a reminder for a task
def get_reminder_time():
        print("\tWeeks -> Days -> Hours:Minutes:Seconds")
        weeks = pyip.inputNum("In how many weeks would you like to be reminded : ", min = 0, max = 51)
        days = pyip.inputNum("In how many days would you like to be reminded : ", min = 0, max = 6)
        reminder_time = pyip.inputTime("How often would you like to be reminded, max value is 23:59:59 : ", formats = ("%H:%M:%S", "%H:%M", "%X"))
        remind_info = [weeks, days, reminder_time.hour, reminder_time.minute, reminder_time.second]
        return remind_info

# gets all of the task info from the user, appends it to a list then returns the list
def get_task_info():
    # empty list for task info
    task_info = []
      
    task_name = pyip.inputStr("\nEnter the task name: ") # get task name from user
    task_info.append(task_name) # append task name to task_info list

    task_completion_status = pyip.inputStr("Enter the task completion status ( Y | N ): ") # get task completion status from user
    checked_completion_status = check_response(task_completion_status)  # check for valid response
    task_info.append(checked_completion_status) # append response to task_info list

    task_reminder_status = pyip.inputStr("Enter if you would like a reminder to be sent ( Y | N ): ") # get task reminder status from user
    checked_reminder_status = check_response(task_reminder_status)  # check for valid response
    task_info.append(checked_reminder_status)   # append response to task_info list
    for i in ('Y','y','Yes','yes'): # loop through responses
        if checked_reminder_status == i:    # check response against loop
            remind_info = get_reminder_time()   # get user variables for reminder information
            # TODO finish reminder functionality

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

# passes task_info list variables into the Task class, then returns the task object
def set_task(task_info):
    task = Task(task_info[0], task_info[1], task_info[2], int(task_info[3]), task_info[4]) # split task_info list into multiple variables and insert into Task class

    return task # return the task object

# TODO allow user to send task list to email or export as txt
if __name__ == '__main__':
    tasks = [] # empty list for task objects to be appended to

    # Prompt user for a file path
    response = pyip.inputStr("Do you have a list file you would like to add to? ( Y | N ) : ")
    check_response(response)
    if response in ('Y','y','Yes','yes'):
        file_name = pyip.inputFilepath("Please enter the full file path : ")
        f = File_Handling(file_name)
        f.handling()
    else:
        file_name = ""

    while True:

        task_info = get_task_info() # gets all tasks info (name, completion status, reminder, priority, comment) then stores it into a variable
        task = set_task(task_info) # breaks task_info into multiple variables and passes that into the Task object, then returns result and stores into a variable

        tasks.append(task) # appending the task object with the user provided data

        # TODO sort tasks based on priority

        # Ask user if they would like to add another task, if not ask if they would like to email the list
        response = pyip.inputStr("\nWould you like to enter another task ( Y | N ): ")
        check_response(response) # check for valid response
        
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
            check_response(response)    # checks user response
            if response in ('Y', 'y', 'Yes', 'yes'):
                email_list(task) # checks response and sends on doesn't send email based on the response
            else:
                print("Task list will not be emailed")   # if the user picks No, tell the user the list will not be emailed
                    

        
            break # break main loop
