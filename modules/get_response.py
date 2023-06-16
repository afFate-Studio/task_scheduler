import pyinputplus as pyip
from modules.check_response import *
from modules.file_handler import *

def ask_user(prompt):
    response = pyip.inputStr(prompt)
    return check_response(response)

def save_file(file_name, sorted_tasks_dict):
    if file_name:
        response = ask_user("\nWould you like to save the new tasks to the file you provided? ( Y | N ): ")
    else:
        response = ask_user("\nWould you like to save your task list to a file ( Y | N ): ")
        if response == 'Y':
            file_name = pyip.inputFilepath("Please enter a file name you would like: ")
    if response == 'Y':
        FileHandling(file_name, sorted_tasks_dict).saving()
    else:
        print("You chose not to save your tasks.")