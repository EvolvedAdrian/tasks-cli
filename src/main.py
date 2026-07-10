"""
main.py is the core file of the Tasks CLI
"""

from .task_manager import TaskManager

task_manager = TaskManager("data/data.json")
task_manager.show_main_menu()

