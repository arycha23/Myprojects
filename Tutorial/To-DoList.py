
task_list = []

while (True):
    task = input("Enter task: ")
    if task == "done":
        break
    task_list.append(task)

print (task_list)
