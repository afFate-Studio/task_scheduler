from os import path
import pyinputplus as pyip

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
        RESPONSES = ['Y','y','Yes','yes','N','n','No','no']
        try:
            if not path.exists(self.file_name):
                raise FileNotFoundError
        except FileNotFoundError:
            while True:
                try:
                    response = input("File not found, would you like to create a new file with the name " + self.file_name + " Y | N: ")
                    for i in range(8):
                        if response in RESPONSES:   # if valid response, ends loop and returns response
                            break
                        else:
                            response = pyip.inputStr("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response
                    
                    if response in RESPONSES[0:3]:
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

                    if isinstance(value, dict):
                        stack.append((value, new_key))
                    else:
                        label = f"{key}"
                        f.write(f"{label}: {str(value)}\n")