def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet.")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(f"{task}\n")

while True:
    action = input("Choose: [view/add/exit] ").lower()
    if action == "view":
        show_tasks()
    elif action == "add":
        task = input("Enter task: ")
        add_task(task)
    elif action == "exit":
        break
