"""
tasks_manager.py contains the TaskManager class, which controlls the tasks logic
"""

import os
import subprocess
import json

from .task import Task

class TaskManager:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file
        self.task_list = self.load_tasks()

    def create_task(self,name):
        self.task_list.append(Task(self.get_next_task_id(),name))
        self.save_tasks()

    def show_tasks(self):
        for task in self.task_list:
            task_status = "[X]" if task.completed else "[]"
            print(f"{task.task_id}. {task.name} {task_status}")

    def find_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id: return task
        return None

    def toggle_completed(self, task_id):
        task = self.find_task(task_id)
        if task: 
            task.completed = not task.completed
            self.save_tasks()

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task: 
            self.task_list.remove(task)
            self.save_tasks()

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

    def json_to_task_list(self, tasks_file):
        try:
            task_list = []
            for json_task in json.load(tasks_file):
                task = Task(json_task["task_id"], json_task["name"], json_task["completed"])
                task_list.append(task)
            return task_list
        except json.decoder.JSONDecodeError:
            return []
    
    def task_list_to_json(self, task_list):
            json_task_list = []
            for task in task_list:
                json_task = task.__dict__
                json_task_list.append(json_task)
            return json_task_list

    def load_tasks(self):
        try: 
            with open(self.tasks_file, "r") as tasks_file:
                return self.json_to_task_list(tasks_file)
        except FileNotFoundError:
            return []
        
    def save_tasks(self):
        with open(self.tasks_file, "w") as tasks_file:
            json.dump(self.task_list_to_json(self.task_list), tasks_file)