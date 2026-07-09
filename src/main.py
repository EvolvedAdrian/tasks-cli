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

    def show_task_options(self, task):
        repeat_menu = True
        while repeat_menu:
            print(f"===== Task {task.task_id} options =====")
            print(f"1. {"Unmark" if task.completed else "Mark"} as complete")
            print(f"2. Delete task")
            print("0. Exit")

            try:
                opt = int(input('\nSelect ---> '))
            except ValueError:
                continue
            
            match opt:
                case 0:
                    pass
                
                case 1:
                    self.complete(task.task_id)
                
                case 2:
                    self.delete(task.task_id)
                
                case _:
                    self.clear_console()
                    continue
            
            repeat_menu = False
            

    def show_menu(self):
        repeat_menu = True
        while repeat_menu:
            self.clear_console()
            last_task_id = self.get_next_task_id()
            print(f"===== Task CLI =====")
            self.show_tasks()
            print("\n---")
            print(f"{last_task_id}. Create a new task")
            print("0. Exit")

            # Check if selected value option is correct
            try:
                opt = int(input('\nSelect ---> '))
            except ValueError:
                continue

            # Check if selected option is valid
            if opt < 0 or opt > last_task_id:
                continue
            self.clear_console()
            
            # IF option is valid
            # Exit
            if opt == 0:
                repeat_menu = False
            
            # Add new task
            elif opt == last_task_id:
                new_task = input("New task: ")
                if new_task:
                    self.create(new_task)
            
            # Access task options
            else:
                self.show_task_options(self.find(opt))

    

task_manager = TaskManager()


