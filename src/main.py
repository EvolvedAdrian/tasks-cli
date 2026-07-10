"""
main.py is the core file of the Tasks CLI
It defines the TaskManager class and the Task class
"""

import os
import subprocess

class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.completed = False

class TaskManager:
    def __init__(self):
        self.task_list = []
        self.show_main_menu()

    def create_task(self,name):
        self.task_list.append(Task(self.get_next_task_id(),name))

    def show_tasks(self):
        for i in self.task_list:
            task_status = "[X]" if i.completed else "[]"
            print(f"{i.task_id}. {i.name} {task_status}")

    def find_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id: return task
        return None

    def toggle_completed(self, task_id):
        task = self.find_task(task_id)
        if task: task.completed = not task.completed

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task: self.task_list.remove(task)

    def get_next_task_id(self):
        return self.task_list[-1].task_id+1 if self.task_list else 1

    def clear_console(self):
        subprocess.call("cls" if os.name == "nt" else "clear", shell=True)

    def check_option(self):
        try:
            return int(input('\nSelect ---> '))
        except ValueError:
            return None

    def show_task_options(self, task):
        while True:
            print(f"===== Task {task.task_id} options =====")
            print(f"1. {"Unmark" if task.completed else "Mark"} as complete")
            print(f"2. delete_task task")
            print("0. Exit")
            
            match self.check_option():
                case 0:
                    pass
                
                case 1:
                    self.toggle_completed(task.task_id)
                
                case 2:
                    self.delete_task(task.task_id)
                
                case _:
                    self.clear_console()
                    continue
            
            break
            

    def show_main_menu(self):
        while True:
            self.clear_console()
            last_task_id = self.get_next_task_id()
            print(f"===== Task CLI =====")
            self.show_tasks()
            print("\n---")
            print(f"{last_task_id}. create_task a new task")
            print("0. Exit")
            
            opt = self.check_option()

            if opt is None: continue
            if opt < 0 or opt > last_task_id: continue
            self.clear_console()
            
            # IF option is valid
            # Exit
            if opt == 0:
                break
            
            # Add new task
            elif opt == last_task_id:
                new_task = input("New task: ")
                if new_task:
                    self.create_task(new_task)
            
            # Access task options
            else:
                self.show_task_options(self.find_task(opt))

    

task_manager = TaskManager()


