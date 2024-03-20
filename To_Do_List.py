def display():
    print('********** WELCOME TO CLI BASED TO DO LIST **********')
    
def userinput():
    print('PLEASE SELECT FROM THE LIST BELOW')
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
        addTask = input("Please Enter the task you want to add: ")
        taskList.append(addTask)
        print("\nTask added successfully!\n")
    elif selection == 2: #Deleting a task
        if len(taskList)==0:
            print("\nNo tasks available in the list.\n")
        else:
            print("Current Tasks:\n", "\n".join([str(i+1)+". "+x for i,x in enumerate(taskList)]))
            index = int(input("Enter the number of the task you want to delete: "))-1
            del taskList[index]
            print("\nTask deleted successfully!\n")
    elif selection == 3: #Displaying all tasks
        if len(taskList)==0:
            print("\nNo tasks available in the list.\n")
        else:
            display()
            print("Tasks:\n", "\n".join([str(i+1)+". "+x for i,x in enumerate(taskList)]))
    elif selection == 4: #Quitting the Program
        print("\nThank You for using To Do List App!\n")
        break
    else:
        print("\nInvalid Selection!\n")

