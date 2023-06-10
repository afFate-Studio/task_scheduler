from tasks import *

# passes task_info list variables into the Task class, then returns the task object
def set_task(task_info):
    task = Task(task_info[0], task_info[1], task_info[2], int(task_info[3]), task_info[4]) # split task_info list into multiple variables and insert into Task class
    task_dict = {
        "name" : task.task,
        "completed" : task.completed,
        "reminder" : task.reminder,
        "priority" : task.priority,
        "comments" : task.comments
    }
    return task_dict # return the task object