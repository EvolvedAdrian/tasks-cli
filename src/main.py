"""
main.py is the core file of the Tasks CLI
It defines the TaskManager class and the Task class
"""

import subprocess

class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.show_menu()

    def create(self,name):
        self.task_list.append(Task(self.get_next_task_id(),name))

    def show_tasks(self):
        for i in self.task_list:
            task_status = "[X]" if i.completed else "[]"
            print(f"{i.task_id}. {i.name} {task_status}")

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

    def get_next_task_id(self):
        return self.task_list[-1].task_id+1 if self.task_list else 1

    def clear_console(self):
        subprocess.call('cls', shell=True)

    def show_menu(self):
        show_menu = True
        while show_menu:
            self.clear_console()
            last_task_id = self.get_next_task_id()
            print(f"===== Task CLI =====")
            self.show_tasks()
            print("\n---")
            print(f"{last_task_id}. Create a new task")
            print(f"0. Exit")

            # Check value error
            try:
                opt = int(input('\nSelect ---> '))
            except ValueError:
                continue

            # Check if selected option is valid
            if opt < 0 or opt > last_task_id:
                continue
            self.clear_console()
            if opt == 0:
                exit()
            elif opt == last_task_id:
                new_task = input("New task: ")
                if new_task:
                    self.create(new_task)

task_manager = TaskManager()


