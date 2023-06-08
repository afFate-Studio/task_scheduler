from os import path
import pyinputplus as pyip

class FileHandling:
    """
        class used to save and write to files
        in order to save tasks as an actual list that a user can refer to
        as well as email the list as a pdf or txt
    """
    def __init__(self, file_name, task=[]):
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
        with open(self.file_name, "a") as f:
            for tasks in self.task:
                f.write("Task Name : ")
                f.write(tasks.task)
                f.write("\nTask Completed Y/N : ")
                f.write(tasks.completed)
                f.write("\nReminder Y/N : ")
                f.write(tasks.reminder)
                f.write("\nTask Priority (0 - 3) : ")
                f.write(str(tasks.priority))
                f.write("\nComments : ")
                f.write(tasks.comments)
                f.write("\n\n")
            f.close()
