from taskmanager import TaskManager

manager = TaskManager()

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter task title: ")
        manager.addTasks(title)
    elif choice == "2":
        manager.list_tasks()
    elif choice == "3":
        manager.list_tasks()
        index = int(input("Enter task number to complete: ")) - 1
        manager.markCompleted(index)
    elif choice == "4":
        manager.list_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        manager.removeTask(index)
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("❗Invalid option. Try again.")
