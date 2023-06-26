import pyinputplus as pyip
from modules.upload_list import *
from modules.get_response import *
from modules.update_task import *
from modules.sorter import *

def check_option(response, file_name=None, tasks_dict={}):
    while True:
        try:
            match response:
                case 0:
                    file_name, tasks_dict = uploadFile()
                    return file_name, tasks_dict
                case 1:
                    file_name = save_file(file_name=file_name, sorted_tasks_dict=tasks_dict)
                    return file_name, tasks_dict
                case 2:
                    if not file_name:
                        file_name, tasks_dict = uploadFile()
                        tasks_dict = (sort(update_task(tasks=tasks_dict)))
                    else:
                        tasks_dict = (sort(update_task(tasks=tasks_dict)))
                    return file_name, tasks_dict
                case 3:
                    quit()
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
    return check_option(pyip.inputNum('Enter your choice: '))

if __name__ == '__main__':
    menu()