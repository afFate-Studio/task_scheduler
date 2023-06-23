import pyinputplus as pyip
from modules.check_response import *
from modules.file_handler import *

def ask_user(prompt):
    response = pyip.inputStr(prompt)
    return check_response(response=response)

def save_file(file_name, sorted_tasks_dict):
    if not file_name:
        file_name = pyip.inputFilepath("Please enter a file name you would like: ")
        return file_name
    FileHandling(file_name=file_name, task=sorted_tasks_dict).saving()
        