FILE_NAME = 'Task.txt'

# function to add a new task
# open file , write and show msg 

print("Name :  Ahsan Raza Talpur ")

# ADD A task            
def Ahsan_add_task(Ahsan_task):
    with open(FILE_NAME, "a") as f:
        f.write(Ahsan_task + "\n")
    print(f"TASK '{Ahsan_task}' Has Been Added")


# another function to view the task  (we use try except in case of our task is empty)

def Ahsan_view_task():
    try:
        with open(FILE_NAME, "r") as f:
            Ahsan_tasks = [task.strip() for task in f if task.strip()]  # remove empty lines
        if not Ahsan_tasks:
            print("No tasks found!")
        else:
            # Professional heading
            print("\n" + "="*50)
            print(" " * 12 + "📋  TASKS OVERVIEW  📋")
            print("="*50 + "\n")
            
            for i, Ahsan_task in enumerate(Ahsan_tasks, start=1):
                print(f"{i}. {Ahsan_task}")
            print("\n" + "="*50 + "\n")
    except FileNotFoundError:
        print("File does not exist")

# update function

def Ahsan_update_task(Ahsan_task_no, Ahsan_new_task):   
    try:
        with open(FILE_NAME, "r") as f:
            Ahsan_tasks = f.readlines()

        if Ahsan_task_no <= 0 or Ahsan_task_no > len(Ahsan_tasks):
            print("Invalid Task")
            return 
       
        Ahsan_tasks[Ahsan_task_no - 1] = Ahsan_new_task + "\n"
        with open(FILE_NAME, "w") as f:
            f.writelines(Ahsan_tasks)

        print(f"Task {Ahsan_task_no} updated Successfully.. to '{Ahsan_new_task}' ")
    except FileNotFoundError:
        print(f"File with task number {Ahsan_task_no} Does not Exist")


# function to delete task
def Ahsan_delete_task(Ahsan_task_no):
    try:
        with open(FILE_NAME, "r") as f:
            Ahsan_tasks = f.readlines()
        if Ahsan_task_no <= 0 or Ahsan_task_no > len(Ahsan_tasks):
            print("Invalid task number ..")
            return
       
        deleted = Ahsan_tasks.pop(Ahsan_task_no - 1)

        with open(FILE_NAME, "w") as f:
            f.writelines(Ahsan_tasks)

        print(f"Task deleted '{deleted.strip()}'")
    except FileNotFoundError:
        print(f"File having task number {Ahsan_task_no} not found")


# function where all function exist and call 
def main():
    while True:
        print("")
        print(" ***                           TO DO LIST  BY AHSAN RAZA TALPUR                        ***")
        print("1. VIEW TASKS")
        print("2. ADD TASK")
        print("3. UPDATE TASK ")
        print("4. DELETE TASK")
        print("5. EXIT")

        try:
            Ahsan_choices = int(input("Enter any number 1 to 5:  "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if Ahsan_choices == 1:
            Ahsan_view_task()
        elif Ahsan_choices == 2:
            Ahsan_task = input("Enter a task: ")
            Ahsan_add_task(Ahsan_task)
        elif Ahsan_choices == 3:
            Ahsan_view_task()
            try:
                Ahsan_task_no = int(input("Enter a task number : "))
                Ahsan_new_task = input("Enter a new task: ") 
                Ahsan_update_task(Ahsan_task_no, Ahsan_new_task)
            except ValueError:
                print("Invalid input")
        elif Ahsan_choices == 4:
            Ahsan_view_task()
            try:
                Ahsan_task_no = int(input("Enter task number to delete: "))
                Ahsan_delete_task(Ahsan_task_no)
            except ValueError:
                print("Invalid input")
        elif Ahsan_choices == 5:
            print("EXITING FROM LIST APPP...........")
            break
        else:
            print("Please enter any number from 1 to 5")


# if you want to run directly
if __name__ == "__main__":
    main()

print("REGARD AHSAN RAZA TALPUR")
