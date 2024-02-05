task=[]



if __name__=="_main_":
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

print("Goodbye wave")



