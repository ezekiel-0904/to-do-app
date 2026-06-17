import json

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return []
    
tasks = load_tasks()

def add_task(task, status):
    tasks.append({"task": task, "status": status})
    print("\n==========================\nTask added successfully!\n==========================")

def view_tasks():
    for i in range(len(tasks)):
        print(f"{i+1}. Task: {tasks[i]['task']}, Status: {tasks[i]['status']}")
    print("\n==========================\nAll tasks displayed successfully!\n==========================")

def update_task(index, status):
    if 0 < index <= len(tasks):
        tasks[index-1]['status'] = status
        view_tasks() 
        print("\n==========================\nTask updated successfully!\n==========================")
    else:
        print("\n==========================\nInvalid task index.\n==========================")

def delete_task(index):
    if 0 < index <= len(tasks):  
        tasks.pop(index-1)
        view_tasks()
        print("\n==========================\nTask deleted successfully!\n==========================")
    else:
        print("\n==========================\nInvalid task index.\n==========================")

while True:
    menu = ["Add Task", "View Tasks", "Update Task", "Delete Task", "Exit"]
    print("\n=== To Do App ===")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print("\n=== Add Task ===")
            task_name = input("Enter task name: ")
            status = "Incomplete"
            add_task(task_name, status)
            save_tasks()
        case "2":
            print("\n=== View Tasks ===")
            view_tasks()
        case "3":
            if not tasks:
                print("\n==========================\nNo tasks available to update.\n==========================")
                continue
            print("\n=== Update Task ===")
            try:
                index = int(input("Enter task index to update: "))
            except ValueError:
                print("\n==========================\nInvalid input. Please enter a number.\n==========================")
                continue
            new_status = input("Enter new status (Complete/Incomplete): ")
            if new_status in ["Complete", "Incomplete"]:
                update_task(index, new_status)
                save_tasks()
            else:
                print("\n==========================\nInvalid status. Please enter 'Complete' or 'Incomplete'.\n==========================")
        case "4":
            if not tasks:
                print("\n==========================\nNo tasks available to delete.\n==========================")
                continue
            print("\n=== Delete Task ===")
            try:
                index = int(input("Enter task index to delete: "))
            except ValueError:
                print("\n==========================\nInvalid input. Please enter a number.\n==========================")
                continue
            delete_task(index)
            save_tasks()
        case "5":
            print("Thanks for using the app. Goodbye!")

            break
        case _:
            print("\n==========================\nInvalid choice. Please try again.\n==========================")