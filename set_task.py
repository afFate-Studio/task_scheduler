
# passes task_info list variables into the Task class, then returns the task object
def set_task(task, completed, reminder, priority, comments):
    task_dict = {
        "name" : task,
        "completed" :completed,
        "reminder" : reminder,
        "priority" : priority,
        "comments" : comments
    }
    return task_dict # return the task object