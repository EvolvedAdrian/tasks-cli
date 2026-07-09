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

    def show_tasks(self):
        for i in self.task_list:
            task_status = "[X]" if i.completed else "[]"
            print(f"--- TASK {i.task_id}. {i.name} {task_status}")

    def find(self, task_id):
        for i in self.task_list:
            actual_task = i
            if actual_task.task_id == task_id: return actual_task
        return None

    def complete(self, task_id):
        task = self.find(task_id)
        if task: task.completed = True

    def delete(self, task_id):
        task = self.find(task_id)
        if task: self.task_list.remove(task)

task_manager = TaskManager()

task_manager.create("Comprar leche")

