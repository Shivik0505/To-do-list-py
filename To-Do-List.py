tasks = []


def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date: ")
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "Incomplete"
    }
    tasks.append(task)
    print("Task created successfully!")


def display_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"Task {i + 1}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Status: {task['status']}")
            print()


def update_task_status():
    display_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        status = input("Enter the new status (Complete/Incomplete): ")
        tasks[task_index]['status'] = status
        print("Task status updated successfully!")
    else:
        print("Invalid task number.")


def delete_task():
    display_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("To-Do List Application")
        print("1. Create Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            update_task_status()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
