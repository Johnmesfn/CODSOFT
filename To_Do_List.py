def display():
    print('********** WELCOME TO CLI BASED TO DO LIST **********')
    
def userinput():
    print('PLEASE SELECT FROM THE MENU BELOW')
    print("1. Add a new task")
    print("2. Delete an existing task")
    print("3. List all tasks")
    print("4. Quit the program")
    user_input = input("Enter your choice: ")
    try:
        return int(user_input)
    except ValueError:
        print("Invalid Input! Please enter a number from 1 to 4.")
        return None

# Task list
taskList=[]

while True:
    selection = userinput()
    if selection == 1: #Adding a new task
        addTask = input("Please Enter the task you want to add: ") #Asking the user the name of the task to add
        taskList.append(addTask) # Task addition to the list 
        print("\nTask added successfully!\n") # Print to the user successful addition of the task
    elif selection == 2: #Deleting a task
        if len(taskList)==0: #If the list is empty or no task is added  do this 
            print("\nNo tasks available in the list.\n") # Printing no task is available in the list
        else: # If there is a task in the list do this
            print("Current Tasks:\n", "\n".join([str(i+1)+". "+x for i,x in enumerate(taskList)])) # Displaying the available tasks in the list
            task_to_delete = input("Enter the number of the task you want to delete: ") # Asking the user to enter the number of the task to delete
            while not task_to_delete.isnumeric(): # Checking whether the user input is numeric or not
                print("Invalid input! Only number is accepted") # Displaying to the user only number is accepted 
                task_to_delete = input("Enter the number of the task you want to delete: ") # Asking the user to enter the number of the task to delete
            while int(task_to_delete) > len(taskList):
                print("Invalid task numner! Please enter a valid task number from the list of task.") # Displaying to the user that the index is invalid
                print("Current Tasks:\n", "\n".join([str(i+1)+". "+x for i,x in enumerate(taskList)])) # Displaying the available tasks in the list
                task_to_delete = input("Enter the number of the task you want to delete: ") # Asking the user to enter the number of the task to delete
                while not task_to_delete.isnumeric(): # Checking whether the user input is numeric or not
                    print("Invalid input! Only number is accepted") # Displaying to the user only number is accepted 
                    task_to_delete = input("Enter the number of the task you want to delete: ") # Asking the user to enter the number of the task to delete
            index = int(task_to_delete)-1 #  Converting user's input into the right index for the list
            try:
                del taskList[index] # Deleting the task the user entered from the list
            except Exception as e:
                print(f"Error! {e}")
            print('\nThe selected task has been deleted successfully!\n') # Displaying deletion was successful
    elif selection == 3: #Displaying all tasks
        if len(taskList)==0: # Do this if there is no task available
            print("\nNo tasks available in the list.\n") # Displaying there is no task available 
        else: # If there is a task in the list do this 
            print("Tasks:\n", "\n".join([str(i+1)+". "+x for i,x in enumerate(taskList)])) # Printing the available task in the list
    elif selection == 4: #If the user selection is Quitting the Program do this 
        print("\nThank You for using To Do List App!\n") # Displaying thank you
        exit() # Exiting the program
    else:
        print("\nInvalid Selection!\n") # If the user selection doesn't belong to any of the Menu Display invalid selection


