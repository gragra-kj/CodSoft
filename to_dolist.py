tasks=[]
def addTask():
    task=input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")
def listTask():
    if not tasks:
        print("There are no tasks available")
    else:
        print("Tasks available: ")
        for index, task in enumerate(tasks,start=1):
            print(f"Tasks #{index}. {task}")
def deleteTask():
    listTask()
    try:
        taskToDelete=int(input("Enter the number to delete"))
        if taskToDelete<=0 and taskToDelete< len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been deleted ")
        else:
            print(f"That {taskToDelete} is not available")

    except:
        print("Invalid input")



if __name__ == "__main__":
    print("Welcome to the to-do list app")
    #while loop for looping the app
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Create a new task")
        print("2. Delete a task")
        print("3. List all your task")
        print("4. Quit")

        select=input("Enter your choice: ")
        if(select=="1"):
            addTask()
        elif(select=="2"):
            deleteTask()

        elif(select=="3"):
            listTask()

        elif(select=="4"):
            break
        else:
            print("Invalid choice")
    print("Goodbye 👋")


