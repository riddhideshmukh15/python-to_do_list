tasks = []

print("Welcome to the Task Management App")

total_task = int(input("Enter how many tasks you want to add = "))

for i in range(1, total_task + 1):
    task_name = input(f"Enter task {i} = ")
    tasks.append({"name": task_name, "status": "Pending"})

while True:
    operation = int(input(
        "\n1 - Add\n"
        "2 - Update\n"
        "3 - Delete\n"
        "4 - View\n"
        "5 - Mark Completed\n"
        "6 - Exit\n"
        "Enter your choice = "
    ))

    if operation == 1:
        add = input("Enter task you want to add = ")
        tasks.append({"name": add, "status": "Pending"})
        print("Task added successfully.")

    elif operation == 2:
        updated_val = input("Enter task name you want to update = ")

        for task in tasks:
            if task["name"] == updated_val:
                up = input("Enter new task = ")
                task["name"] = up
                print("Task updated successfully.")
                break
        else:
            print("Task not found.")

    elif operation == 3:
        del_val = input("Which task do you want to delete = ")

        for task in tasks:
            if task["name"] == del_val:
                tasks.remove(task)
                print("Task deleted successfully.")
                break
        else:
            print("Task not found.")

    elif operation == 4:
        print("\n===== YOUR TASKS =====")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} [{task['status']}]")

    elif operation == 5:
        task_name = input("Enter task name to mark as completed = ")

        for task in tasks:
            if task["name"] == task_name:
                task["status"] = "Completed"
                print("Task marked as completed!")
                break
        else:
            print("Task not found.")

    elif operation == 6:
        print("Closing the program...")
        break

    else:
        print("Invalid choice.")