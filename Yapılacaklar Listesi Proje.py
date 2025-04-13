# To-Do List Project

options = ["add task", "mark as completed", "delete task", "show tasks", "exit"]

tasks = []

while True:  # Loop to keep the program running
    UserInput = input(f"Select an option ({', '.join(options)}): ").lower()

    if UserInput == "add task":
        task = input("Enter the task: ").lower()
        tasks.append(task)
        print(f"Task '{task}' has been added to your to-do list.")

    elif UserInput == "mark as completed":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            task = input("Enter the task to mark as completed: ").lower()
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' has been marked as completed and removed from the list.")
            else:
                print(f"Task '{task}' not found in your to-do list.")

    elif UserInput == "delete task":
        task = input("Enter the task to delete: ").lower()
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' has been deleted from the list.")
        else:
            print(f"Task '{task}' not found in your to-do list.")

    elif UserInput == "show tasks":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for task in tasks:
                print(f"- {task}")

    elif UserInput == "exit":
        print("Exiting the program. Goodbye!")
        break

    elif UserInput == "clear":
        if len(tasks) == 0:
            print("Your to-do list is already empty.")
        else:
            print("Are you sure you want to clear all tasks? (yes/no)")
            confirm = input().lower()
            if confirm == "yes":
                tasks.clear()
                print("All tasks have been cleared from your to-do list.")
            else:
                print("Clear operation cancelled.")
    else:
        print("Invalid option selected. Please try again.")

