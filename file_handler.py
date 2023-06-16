from os import path
import pyinputplus as pyip
from check_response import *
from set_task import *

class FileHandling:
    """
        class used to save and write to files
        in order to save tasks as an actual list that a user can refer to
        as well as email the list as a pdf or txt
    """
    def __init__(self, file_name, task={}):
        self.file_name = file_name
        self.task = task

    def handling(self):
        try:
            if not path.exists(self.file_name):
                raise FileNotFoundError
            else:
                with open(self.file_name, 'r') as f:
                    lines = f.readlines()
                    f.close()
                
                task_info = {}
                for line in lines:
                    line = line.strip()
                    if ':' in line:
                        key, value = line.split(':', 1)
                        task_info[key.strip()] = value.strip()

                set_task(task_info)

        except FileNotFoundError:
            while True:
                try:
                    response = input("File not found, would you like to create a new file with the name " + self.file_name + " Y | N: ")
                    check_response(response=response)
                    
                    if response in 'Y':
                        f = open(self.file_name, "x")
                        f.close()
                        break
                    else:
                        self.file_name = ""
                        return self.file_name
                except ValueError:
                    pass

    def saving(self):
        # takes tasks_dict appends it to the list stack
        stack = [(self.task, '')]

        with open(self.file_name, "a") as f:
            while stack:
                # takes current_dict and parent_key from the stack
                current_dict, parent_key = stack.pop()

                # traverse the nested dictionary
                for key, value in current_dict.items():
                    new_key = f"{parent_key}.{key}" if parent_key else key

                    # sets a new key if a new dictionary is reached
                    if isinstance(value, dict):
                        stack.append((value, new_key))
                    else:
                        # sets a label for the values
                        label = f"{key}"
                        # writes to the provided file name
                        f.write(f"{label} : {str(value)}\n")
                        if label == 'comments':
                            f.write('\n')
