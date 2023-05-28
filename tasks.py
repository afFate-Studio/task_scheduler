
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
        if ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes':
            self.completed = 'Y'
        elif ans == 'N' or ans == 'n' or ans == 'No' or ans == 'no':
            self.completed = 'N'
        else:
            return "Invalid selection, please type Y or N"
    
    #TODO reminders function - to actually send out a reminder 
    def set_reminder(self,ans):
        test_case = ['y','Y','yes','n','N','no']
        for i in test_case:
            if ans != i:
                return "Invalid selection, please type Y or N"
            else:
                break
            
        if ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes':
            self.reminder = 'Y'
            # TODO ask when to be reminded week/day/hour/miniute
        elif ans == 'N' or ans == 'n' or ans == 'No' or ans == 'no':
            self.reminder = 'N'
        
    # sets priority of a task
    def set_priority(self,ans):
        priority = [0,1,2]
        for i in priority:
            if ans == i:
                self.priority = i    
        return "Invalid selections, please type 0 - 2, 0 being lowest priority 2 being highest priority"

    # sets the comments for a task
    def set_comment(self,comments):
        self.comments = comments