"""
main.py is the core file of the Tasks CLI
It defines the TaskManager class and the Task class
"""

class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_list = []

    def create(self,name):
        task_id = self.task_list[-1].task_id+1 if self.task_list else 1
        self.task_list.append(Task(task_id,name))

    def see_all(self):
        for i in self.task_list:
            task_status = "[X]" if i.completed else "[]"
            print(f"--- TASK {i.task_id}. {i.name} {task_status}")

task_manager = TaskManager()

task_manager.create("Comprar leche")

task_manager.see_all()