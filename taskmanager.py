import json
import os
from pathlib import Path

from tasks import Task


class TaskManager:
    def __init__(self, path="./data/todo-data.json"):
        self.path = Path(path)
        self.tasks = []
        self._loadTasks()

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✅" if task.completed else "❌"
            print(f"{i}. {task.description} [{status}]")

    def addTasks(self, descr):
        new_task = Task(descr)
        self.tasks.append(new_task)
        self._saveTask()

    def markCompleted(self, index):
        if index < 0 or index >= len(self.tasks):
            print("❗Invalid task number.")
            return
        self.tasks[index].viaCompleted()
        self._saveTask()
        print(f"🎉 Task completed: {self.tasks[index].description}")

    def removeTask(self, index):
        if index < 0 or index >= len(self.tasks):
            print("❗Invalid task number.")
            return
        removed = self.tasks.pop(index)
        self._saveTask()
        print(f"🗑️ Task deleted: {removed.description}")

    def _saveTask(self):
        data = [task.toJson() for task in self.tasks]
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def _loadTasks(self):
        try:
            if not self.path.exists() or self.path.stat().st_size == 0:
                self.tasks = []
                return
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Initializing empty task list.")
            self.tasks = []
        except FileNotFoundError:
            print("tasks.json not found. Initializing empty task list.")
            self.tasks = []
