import json

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

# View all tasks
def view_tasks(tasks):
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")
    print()

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter task number to mark as done: "))
    tasks[task_no - 1]["completed"] = True
    print("Task updated!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter task number to delete: "))
    tasks.pop(task_no - 1)
    print("Task deleted!")

# Main menu
def menu():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    menu()

