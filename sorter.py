
# https://realpython.com/iterate-through-dictionary-python/#using-comprehensions
def sort(tasks_dict, LENGTH):
    sorted_dict = dict(sorted(tasks_dict.items(), key=lambda item: item[0], reverse=True))

    print(sorted_dict)

        

#print(dict(sorted(tasks_dict.items(), key=sort, reverse=True)))