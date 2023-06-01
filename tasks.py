
# class used to set a task based on information passed on by user
class Task:

    # initializing the variables
    def __init__(self,task,completed='', reminder='',priority=0, comments=''):
        self.task = task
        self.completed = completed
        self.reminder = reminder
        self.priority = priority
        self.comments = comments
    
    # used to print(task)
    def __str__(self):
        return f'Task: {self.task}\nCompletion status: {self.completed}\nReminder set: {self.reminder}\nPriority: {self.priority}\nComments: {self.comments}'

    # sets completion status of a task
    def complete_task(self,ans):
        if ans in ('Y', 'y', 'Yes', 'yes'):
            self.completed = 'Y'
        else:
            self.completed = 'N'
    
    #TODO reminders function - to actually send out a reminder 
    def set_reminder(self,ans):           
        if ans in ('Y', 'y', 'Yes', 'yes'):
            self.reminder = 'Y'
            # TODO ask when to be reminded week/day/hour/miniute
        else:
            self.reminder = 'N'
        
    # sets priority of a task
    def set_priority(self,ans):
            self.priority = ans

    # sets the comments for a task
    def set_comment(self,comments):
        self.comments = comments