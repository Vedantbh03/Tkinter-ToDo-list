def view_list(todo):
    print("YOUR TO DO LIST:\n")
    num = 1
    for i in todo:
        print(f'{num}: {i}\n')
        num += 1
    return 0


def add_task(todo):
    task = str(input("Please enter a task to complete:\n"))
    todo.append(task)
    view_list(todo)
    return 0

def remove_task(todo):
     view_list(todo)
     remove = int(input("\nEnter the number of the task you want to remove!\n"))
     todo.pop(remove)
     print("Task removed successfully!\n")
     view_list(todo)
     return 0
     


def main():
    print("Welcome to the TO-DO List!\n")
    option = 1
    todo = []
    while option != 0:
        option = int(input("Pick a option in the directory or press 0 to exit:\n 1: Add a new task\n 2: Remove a completed task\n 3: View current list\n"))
        if option == 1:
            add_task(todo)
        elif option == 2:
            remove_task(todo)
        else:
            view_list(todo)
if __name__ == "__main__":
    main()