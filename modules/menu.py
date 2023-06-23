import pyinputplus as pyip
from modules.upload_list import *
from modules.get_response import *
from modules.upload_list import *

def check_option(response):
    while True:
        try:
            match response:
                case 0:
                    file_name, tasks_dict = uploadFile()
                    return file_name, tasks_dict
                case 1:
                    print('make a new task file')
                    save_file(file_name=file_name, sorted_tasks_dict=sorted_tasks_dict)
                case 2:
                    # if file was uploaded or created
                    print('update task')
                    break
                case 3:
                    print('exit')
                    break
                case _:
                    print('invalid choice')
                    raise ValueError
        except ValueError:
            response = pyip.inputNum('Enter a number for testing 0 - 3: ')

def menu():
    print('Enter a menu option to continue...')
    print('0 -> Upload a file')
    print('1 -> Make a new file')
    print('2 -> Update a task')
    print('3 -> To Exit the application')
    check_option(pyip.inputNum('Enter your choice: '))
    
if __name__ == '__main__':
    menu()