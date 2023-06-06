# class used to set a task based on information passed on by user
from reminder import Reminder

class Task:

    # initializing the variables
    def __init__(self, task, completed='', reminder='', priority=0, comments=''):
        self.task = task
        self.completed = completed
        self.reminder = reminder
        self.priority = priority
        self.comments = comments
    
    # used to print(task)
    def __str__(self):
        return f'Task: {self.task}\nCompletion status: {self.completed}\nReminder set: {self.reminder}\nPriority: {self.priority}\nComments: {self.comments}'
    