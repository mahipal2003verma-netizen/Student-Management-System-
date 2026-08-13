tasks = []


def add_task():
    print("\n----- ADD TASK -----")

    task_name = input("Enter task: ")

    if task_name.strip() == "":
        print("Task cannot be empty.")
        return

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully! ✅")


def view_tasks():
    print("\n----- ALL TASKS -----")

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed ✅"
        else:
            status = "Pending ⏳"

        print(f"{i}. {task['name']} - {status}")


def complete_task():
    print("\n----- COMPLETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_no = int(input("Enter task number to complete: "))

        if task_no >= 1 and task_no <= len(tasks):

            tasks[task_no - 1]["completed"] = True

            print("Task marked as completed! ✅")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    print("\n----- DELETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_no = int(input("Enter task number to delete: "))

        if task_no >= 1 and task_no <= len(tasks):

            deleted = tasks.pop(task_no - 1)

            print("Task deleted successfully! 🗑️")
            print("Deleted:", deleted["name"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def search_task():
    print("\n----- SEARCH TASK -----")

    search = input("Enter task name to search: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):

        if search in task["name"].lower():

            if task["completed"]:
                status = "Completed ✅"
            else:
                status = "Pending ⏳"

            print(f"{i}. {task['name']} - {status}")

            found = True

    if not found:
        print("No matching task found.")


while True:

    print("\n==============================")
    print("       TO-DO LIST APP")
    print("==============================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Search Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        search_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("\nThank you for using To-Do List App! 👋")
        break

    else:
        print("Invalid choice! Please try again.")