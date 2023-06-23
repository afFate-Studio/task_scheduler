import pyinputplus as pyip
from modules.file_handler import *

def uploadFile():
    file_name = pyip.inputFilepath("Please enter the full file path : ")
    tasks_dict, file_name = FileHandling(file_name).handling()    # tasks file path and sets the variable & checks if file exists, if it doesn't exists prompts user to make the file   

    return file_name, tasks_dict