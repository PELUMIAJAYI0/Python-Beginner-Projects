tasks = []  # Initialize an empty list to store tasks

name = input("Enter your name---> ")
while True:
    print(f"...{name.capitalize()} Welcome to the To Do List App...")
    print("1. Add Task")
    print("2. List all Tasks")
    print("3. Mark Task as done")
    print("4. Delete a task")
    print("5. Exit App")

    choice = input(f"{name.capitalize()} Enter your choice---> ")

    if choice == "1":
        print("...Add Task...")
        number_of_tasks = int(input(f"{name.capitalize()} How many tasks do you want to add---> "))

        for i in range(number_of_tasks):
            task_description = input(f"{name.capitalize()} Enter your task---> ")
            task = {"task": task_description, "done": False}
            tasks.append(task)
            print("Task Added...")

    elif choice == "2":
        print("...List of all Tasks...")
        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks):
                status = "Done" if task['done'] else "Not done"
                print(f"{index + 1}. {task['task']} - {status}")

    #The next section allows the user to mark a task as done by entering the task number.
    elif choice == "3":
        task_index = int(input(f"{name.capitalize()} Enter the task number to mark as done---> "))
        if 0 <= task_index - 1 < len(tasks):
            tasks[task_index - 1]["done"] = True
            print("Task marked as done.")
        else:
            print(f"You entered an invalid task number, {name.capitalize()}")

    #The following section allows the user to delete a task by entering the task number.
    elif choice == "4":

        print("...List of all Tasks...")
        for index, task in enumerate(tasks):
            status = "Done" if task['done'] else "Not done"
            print(f"{index + 1}. {task['task']} - {status}")
            
        task_to_delete = int(input(f"{name.capitalize()} Enter the task number you want to delete---> "))
        if 0 <= task_to_delete - 1 < len(tasks):
            tasks.pop(task_to_delete - 1)
            print(f"{name.capitalize()} Task deleted.")
        else:
            print(f"{name.capitalize()} Entered an Invalid task number")
    
    #The final section handles the user's choice to exit the application.
    elif choice == "5":
        print(f"{name.capitalize()} Exiting the To Do List App, Have a Great Day...")
        break

    else:
        print(f"{name.capitalize()} Invalid choice, please try again")

    # prompts the user to continue using the application or exit.
    cont = input(f"{name.capitalize()}, do you want to continue (yes/no)---> ").lower()
    if cont != "yes":
        print(f"{name.capitalize()} Exiting the To Do List App, Have a Great Day...")
        break
