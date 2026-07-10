"""
tasks.py contains the Task class, which represents every single task with its properties
"""

class Task:
    def __init__(self, task_id, name, completed=False):
        self.task_id = task_id
        self.name = name
        self.completed = completed