from os import path
import pyinputplus as pyip
from modules.check_response import *
from modules.set_task import *
from modules.tasks import *

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
            # raises a FileNotFoundError if no file is found
            if not path.exists(self.file_name):
                raise FileNotFoundError
            else:
                # opens the provided file, reads it and stores the information into a variable
                with open(self.file_name, 'r') as f:
                    lines = f.readlines()
                    f.close()
                
                # empty list to add file info into
                tasks = {}
                current_task = {}
                # goes line by line spliting the key : value pair by looking for ':' in the str
                for line in lines:
                    line = line.strip()
                    if line and ':' in line:
                        key, value = line.split(':', 1)
                        current_task[key.strip()] = value.strip()
                    else:
                        tasks.update(Task(tasks, current_task))   
                        current_task = {}

                return tasks, self.file_name
            
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
                        self.file_name = None
                        return self.file_name, self.task
                except ValueError:
                    pass

    def saving(self):
        # takes tasks_dict appends it to the list stack
        stack = [(self.task, '')]

        with open(self.file_name, "w") as f:
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
