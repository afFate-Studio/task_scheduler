# TODO 
# print all of the task names
# allow user to put one of the tasks based on its name
# print all of the task's elements
# allow user to change what they want in the task
# update the selected task in the dictionary
import pyinputplus as pyip

def update_task(tasks):
    print('Please select a task you would like to edit based on it\'s name: ')
    for dict, info in enumerate(tasks):
        print(tasks[info]['name'])
    user_task = pyip.inputStr('Which task would you like to update: ')

    # TODO allow user to edit
    for dict, info in enumerate(tasks):
        if user_task == tasks[info]['name']:
            print(user_task)

    return tasks