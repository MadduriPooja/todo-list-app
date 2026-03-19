tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    tasks.pop(index-1)

while True:
    print("\nOptions: 1. Add  2. Show  3. Delete  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "4":
        break