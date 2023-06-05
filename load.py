# class used to save and write to files
# in order to save tasks as an actual list that a user can refer to
# as well as email the list as a pdf or txt
class File_Handling:
    def __init__(self, file_name, task):
        self.file_name = file_name
        self.task = task

    def handling(self):
        try:
            with open(self.file_name, "a") as f:
                f.write(self.task)
                f.close()
        except FileNotFoundError:
            while True:
                try:
                    response = input("File not found, would you like to create a new file with the name " + self.file_name + " Y | N: ")
                    for i in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
                        if response == i:   # if valid response, ends loop and returns response
                            if i in ('Y', 'y', 'Yes', 'yes'):
                                f.open(self.file_name, "x")
                                with open(self.file_name, "a") as f:
                                    f.write(self.task)
                                    f.close()
                                break
                            else:
                                print("You chose not to create a new file with the name " + self.file_name)
                                break
                    response = input("Please enter a valid selection ( Y | N ): ")  # otherwise prompts user to input a new response then checks new response
                except ValueError:
                    pass
                
