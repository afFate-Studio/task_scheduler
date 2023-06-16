
# https://realpython.com/iterate-through-dictionary-python/#using-comprehensions
def sort(tasks_dict):
    # sort dictionary based on the 'priority' key in the nested dictionary
    sorted_dict = dict(sorted(tasks_dict.items(), key=lambda item: int(item[1]['priority'])))

    return sorted_dict