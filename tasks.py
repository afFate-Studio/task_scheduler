def Task(tasks_dict, task):
    LENGTH = len(tasks_dict) # Updated every loop with the list length, not exactly a constant

    # check the length of the dictionary and updates it according    
    if len(tasks_dict) == 0:
        tasks_dict.update({"Task0" : { "name" : task["name"],
                                    "completed" : task["completed"],
                                    "reminder" : task["reminder"],
                                    "priority" : task["priority"],
                                    "comments" : task["comments"]
                                    }})     
    else:
        
        tasks_dict.update({"Task" + str(LENGTH) : {"name" : task["name"],
                                                "completed" : task["completed"],
                                                "reminder" : task["reminder"],
                                                "priority" : task["priority"],
                                                "comments" : task["comments"]
                                                }})
        
    return tasks_dict