#Your todo tracker should do the following: 
          #Display the current list of todos 
          #Allow the user to add new todo items
          #Allow the user to remove existing todo items
#Start!!!
def main():
    # Load existing tasks from file
    try:
        with open("todo_proj.txt", "r") as file:
            tasks = file.readlines()  # Read tasks from the file
    except FileNotFoundError:
        tasks = []  # Start with an empty task list if the file doesn't exist

    while True:
        print("\nWelcome to the Dawgs To-Do Tracker!!")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Your current tasks are:')
        for task in tasks:
            print(f'- {task.strip()}')  # Display each task on a new line 

    addrrem = input("Would you like to add or remove a task? (type 'LEAVE' to quit): ").strip().lower()
    
    if addrrem == "add":
        addtask = input("Add a task here: ").strip()
        tasks.append(addtask)  # Added the new task to the list
        print(f'Task "{addtask}" added.')
    
    elif addrrem == "remove":
        remtask = input("Type the task you want to remove: ").strip()
        if remtask in tasks:
            tasks.remove(remtask)  # Removed the task from the list
            print(f'Task "{remtask}" removed.')
        else:
            print(f'Task "{remtask}" not found in the list.')
    
        elif addrrem == "leave":
            with open("todo_proj.txt", "w") as file:
                file.writelines(tasks)  # Write the current tasks to the file
            print("Exiting the Dawgs To-Do Tracker. Goodbye!")
            break  # Exit the loop

    else:
        print("Invalid option. Please type 'add', 'remove', or 'LEAVE!'.")
