#Your todo tracker should do the following: 
          #Display the current list of todos 
          #Allow the user to add new todo items
          #Allow the user to remove existing todo items
#Start!!!
print("Welcome to the Dawgs To-Do Tracker!!")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
tasks = ["get cash", "spend cash", "play ot7quanny"]
while True:
    print('Your current tasks are: ' + ', '.join(tasks))
    
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
    
    elif addrrem == "exit":
        print("Exiting the Dawgs To-Do Tracker. Til We BARK! Paths Again!")
        break
    
    else:
        print("Invalid option. Please type 'add', 'remove', or 'LEAVE!'.")
