import datetime
import os

while True:
    print("\n ==== To Do List App.CLI ====")
    print("Choices: ")
    print("1. Add Task")
    print("2. See Task")
    print("3. Mark Task as Done")
    print("4. Delete all task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    #Add task
    if (choice == 1):
        try:
            task = input("\n Add your task: ")

            if (task.strip() == ""):
                raise ValueError("Task Is Empty")

            time = datetime.datetime.now()
            formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")

            with open("task.txt", "a") as f:
                f.write(f"[ ][{formatted_time}] {task} \n")

            print("Task succesfully noted! \n")

        except ValueError as e:
            print("Failed", e)

    # See task
    elif (choice == 2):
        print("\n== Your Task ==")
        try:
            with open("task.txt", "r") as f:
                tasks = f.readlines()

                if not tasks:
                    print("There is no task avalaible :)")
                else:
                    for index, line in enumerate(tasks, start=1):
                        print(f"{index}. {str(line).strip()}")
        except FileNotFoundError:
            print("There is no task avalaible!")

    # Mark task
    elif (choice == 3):
        try:
            with open("task.txt", "r") as f:
                tasks = f.readlines()

            if not tasks:
                print("There is no task to be marked!")
            else:
                print("\n==Your Task==")
                for index, line in enumerate(tasks, start=1):
                    print(f"{index}. {str(line).strip()}")

            task_number = int(input("Enter task number: "))

            if (task_number < 1 or task_number > len(tasks)):
                print("Invalid task number")
            else:
                if "[#]" in tasks[task_number - 1]:
                    print("Task already be done")
                else:
                    tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[#]", 1)

                    with open("task.txt", "w") as f:
                        f.writelines(tasks)

                    print("Task Are marked complete!")
        except FileNotFoundError:
            print("There is no task avalaible!")

    # delete all tasks
    elif (choice == 4):
        if (os.path.exists("task.txt")):
            confirm = input("Are you sure want to delete all tasks? (y/n): ")

            if (confirm.lower() == "y"):
                os.remove("task.txt")
                print("All task already deleted")
            else:
                print("Delete is canceled")
        else:
            print("There is no task to be deleted")

    #
    elif (choice == 5):
        print("\n Thankyou for using this:)")
        break

    else:
        print("Invalid Option")





    
        
        

    