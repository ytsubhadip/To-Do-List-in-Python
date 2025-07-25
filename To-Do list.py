
def add_task(task_list):
    task = str(input("Enter your task: ")).lower()
    task_list.append(task)
    save_file(task_list)
    print("Save Task ...\n")


def display_task(task_list):
    if not task_list:
        print("Your ToDo list is empty")
    else:
        print("Your all task")
        a = 1
        for task in task_list:
            print(f"{a}-{task}")
            a=a+1
        print("\n")


def remark_task(task_list, c_task):
    # clear the complete task list
    c_task.clear()
    # load file
    try:
        with open("complete_task_file.txt", "r") as f:
            for line in f:
                c_task.append(line.strip())

    except FileNotFoundError:
        pass

    a = 1
    print("Your total task: ")
    for task in task_list:
        print(f"{a}-{task}")
        a = a + 1

    if not c_task:
        print("You don't have complete any task\n")
    else:
        # display your complete task
        n = 1
        print("\nYour complete task: ")
        for task in c_task:
            print(f"{n}-{task}")
            n = n + 1

    try:
        index = int(input("Enter your complete task index from your total task: "))
        selected_task = task_list[index - 1]

        if selected_task not in c_task:
            c_task.append(selected_task)

            with open("complete_task_file.txt", "w") as file:
                for task in c_task:
                    file.write(f"{task}\n")
        else:
            print("This task is already marked as completed.")

    except Exception as E:
        print(f"some error occurs : {E}")

    


def delete_task(task_list):
    a = 1
    print("Your All Task : ")
    for task in task_list:
        print(f"{a}-{task}")
        a=a+1
    print()
    print("Enter your task index you want to delete: ")
    index = int(input())
    task_list.remove(task_list[index-1])
    save_file(task_list)


def save_file(task_list):

    try:
        with open("task_save_file.txt", "w") as file:
            for task in task_list:
                file.write(f"{task}\n")

    except FileNotFoundError:
        print("File not found")

def  load_task_in_file(task_list):
    try :
        with open("task_save_file.txt","r") as file:
            for line in file:
                task_list.append(line.strip())

    except FileNotFoundError:
        print("Your file is missing")
    return  task_list


if __name__ == "__main__":

    todo = []
    remark_list = []
    load_task_in_file(todo)
    print("===== Your Daily To-Do List =====")
    while True:
        print("Manu Bar: ")
        print("1. View all task")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("7. Exit")
        print("==================================")
        user_choice= int(input("Enter your choice: "))

    #condition

        if user_choice == 7:
            print("Thanks For Use \nDeveloped By YT SUBHADIP")
            break

        elif user_choice == 1:
            print()
            display_task(todo)

        elif user_choice == 2:
            add_task(todo)

        elif user_choice == 3:
            remark_task(todo, remark_list)

        elif user_choice == 4:
            delete_task(todo)




