from tasks import *

# passes task_info list variables into the Task class, then returns the task object
def set_task(task_info):
    task = Task(task_info[0], task_info[1], task_info[2], int(task_info[3]), task_info[4]) # split task_info list into multiple variables and insert into Task class

    return task # return the task object