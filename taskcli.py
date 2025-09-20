import sys
import json

tasklist = []
next_id = 1
#file reading
try:
#storing the tasklist array
    with open ("taskcli.json") as tasks:
        tasklist = json.load(tasks) 
#storing the next task id so when we add_task() it knows which id to use
    with open ("taskcli_id.json") as tasks:
        next_id = json.load(tasks) #storing the next_id
except FileNotFoundError:
    pass
class Task:
    def __init__(self, description, status="todo"):
        global next_id #to change the next_id
        self.description = description
        self.status = status
        self.id = next_id
        next_id += 1
    def to_dict(self): #since you cant append classes to json, you have to do this
        return {"description": self.description, "status": self.status, "ID": self.id}
def add_task(description):
#ex: python taskcli.py taskcli add "become indonesian"
    task = Task(description)
    print(f"Task created: {task.description} | Status: {task.status} | (ID: {task.id})")
    task = task.to_dict()
    tasklist.append(task)
    return task
def delete_task(task_id, next_id):
#ex: python taskcli.py taskcli delete 1
    for task in tasklist:
        if task.get("ID") == task_id:
            tasklist.remove(task)
            print("Task Deleted")
# if the user removes all tasks, the next_id will be reset back to 1
    if len(tasklist) == 0:
        return 1
    else:
        return next_id
def update_task(updated_description, task_id):
#ex: python taskcli.py taskcli update 1 "convert to islam"
    for task in tasklist:
        if task.get("ID") == task_id:
            task["description"] = updated_description
            print("Task Updated")
def clear_tasklist():
#ex: python taskcli.py taskcli clear
    print("Tasklist cleared")
    return [], 1
def list_tasklist():
#ex: python taskcli.py taskcli list
    print("The current tasklist:")
    for dictionary in tasklist:
        print(dictionary)
    
def mark_task(updated_status, task_id):
    if task_id != "everything":
        for task in tasklist:
            if task.get("ID") == task_id:
                task["status"] = updated_status
        print(f"Task marked as {updated_status}")
    else:
        for task in tasklist:
            task["status"] = updated_status
        print(f"All tasks marked as {updated_status}")
# if statement spam to see what the user wants to do
if sys.argv[1] == "taskcli":
    if sys.argv[2] == "add":
        print(sys.argv[3])
        add_task(sys.argv[3])
        list_tasklist()
    elif sys.argv[2] == "delete":
        try:
            task_id = int(sys.argv[3])
            next_id = delete_task(task_id, next_id)
        except ValueError:
            print("put in a number for the task id next time")
        finally:
            list_tasklist()
    elif sys.argv[2] == "clear":
        tasklist, next_id = clear_tasklist()
    elif sys.argv[2] == "list":
        if len(sys.argv) < 4:
            list_tasklist()
        else:
            if sys.argv[3] == "todo":
                filtered_tasklist = [task for task in tasklist if task.get("status") == "todo"]
            elif sys.argv[3] == "in-progress":
                filtered_tasklist = [task for task in tasklist if task.get("status") == "in-progress"]
            elif sys.argv[3] == "done":
                filtered_tasklist = [task for task in tasklist if task.get("status") == "done"]
            print("The filtered tasklist:")
            for task in filtered_tasklist:
                print(task)
    elif sys.argv[2] == "update":
        try:
            task_id = int(sys.argv[3])
            updated_description = sys.argv[4]
            update_task(updated_description, task_id)
        except ValueError:
            print("put in a number for the task id next time")
        finally:
            list_tasklist()
    elif sys.argv[2] == "mark":
        try:
            updated_status = sys.argv[4].lower()
            available_commands =["done", "in-progress", "todo"]
            if sys.argv[3] == "everything":
                task_id = "everything"
            else:
                task_id = int(sys.argv[3])            
            if updated_status in available_commands:
                mark_task(updated_status, task_id)
            else:
                print(f'''
                "{sys.argv[4]}" is not a vaild command, available commands include:
                - done (marks tasks as done)
                - in-progress (marks tasks as in progress)
                - todo (marks tasks as todo)
                ''')
        except ValueError:
            print("put in an actual number for task id next time")
        finally:
            list_tasklist()
    else:
        print(f'''
        "{sys.argv[2]}" is not a valid command, available commands include:
        - add (adds a task, ex: taskcli add "go get groceries")
        - delete (deletes a task, ex: taskcli delete 1)
        - clear (clears the tasklist, ex: taskcli clear)
        - list (lists the tasklist, ex: taskcli list)
        - update (updates a task description, ex: taskcli update 1 "go play guitar"
        - mark (marks a task as in-progress or done or todo, ex: taskcli mark 1 in-progress)
              ''')
else:
   print("put taskcli first before the commands")

#saving the tasklist and the next_id so it doesnt reset back to 1
with open ("taskcli.json", "w") as tasks:
    json.dump(tasklist, tasks, indent=4)
with open ("taskcli_id.json", "w") as tasks:
    json.dump(next_id, tasks)