"""
Tests file : Arrange --> Act --> Assert
"""

import unittest
import json

from src.task_manager import TaskManager

TEST_FILE = "tests/data_test.json"

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Arrange --> prepare environment before tests
        with open(TEST_FILE, "w") as f:
            f.write("")
        
        self.manager = TaskManager(TEST_FILE)
        self.manager.create_task("Task")
    
    def get_first_task(self):
        with open(TEST_FILE, "r") as task_file:
            try:
                stored_tasks = json.load(task_file)[0]
            except IndexError:
                stored_tasks = {}
        
        try:
            memory_tasks = self.manager.task_list[0].__dict__
        except IndexError:
            memory_tasks = {}

        return (stored_tasks,memory_tasks)

    def test_create_task(self):
        self.assertEqual(len(self.manager.task_list), 1)

    def test_get_next_task_id(self):
        # Act --> Get next task_id
        next_task_id = self.manager.get_next_task_id()

        self.assertEqual(next_task_id, 2)

    def test_autoincremental_task_id(self):
        self.assertEqual(self.manager.task_list[-1].task_id, 1)

        self.manager.create_task("New task")

        self.assertEqual(self.manager.task_list[-1].task_id, 2)

        self.manager.create_task("Last task")

        self.assertEqual(self.manager.task_list[-1].task_id, 3)

    
    def test_toggle_completed(self):
        self.assertFalse(self.manager.task_list[0].completed)
        
        # Act --> Toggle completed
        self.manager.toggle_completed(1)

        self.assertTrue(self.manager.task_list[0].completed)

        # Act --> Toggle completed
        self.manager.toggle_completed(1)

        self.assertFalse(self.manager.task_list[0].completed)
    
    def test_delete_task(self):
        # Act --> Delete task
        self.manager.delete_task(1)

        self.assertEqual(self.manager.task_list, [])

    def test_find_existing_task(self):
        # Act --> Find existing task
        founded_task = self.manager.find_task(1)

        self.assertIsNotNone(founded_task)

    def test_find_non_existing_task(self):
        # Act --> Check non existing task was not found
        self.assertIsNone(self.manager.find_task(999))

    def test_delete_impossible_task(self):
        # Act --> Delete non existing task
        self.manager.delete_task(999)

        self.assertEqual(len(self.manager.task_list), 1)
    
    def test_toggle_impossible_task(self):
        # Act --> Toggle non existing task
        self.manager.toggle_completed(999)

        self.assertFalse(self.manager.task_list[0].completed)

    def test_task_persistence_after_creation(self):
        # Act --> Action to check persistence on task creation
        # first_task[0] = STORED ON JSON
        # first task[1] = MEMORY TASK (NOT PERSISTED)
        first_task = self.get_first_task()

        self.assertDictEqual(first_task[0], first_task[1])

    def test_task_persistence_after_toggle_completion(self):
        # Act --> Action to check persistence on toggle completed
        self.manager.toggle_completed(1)

        first_task = self.get_first_task()

        self.assertDictEqual(first_task[0], first_task[1])

    def test_task_removed_after_deletion(self):
        # Act --> Action to check persistence on task deletion
        self.manager.delete_task(1)

        first_task = self.get_first_task()

        self.assertDictEqual(first_task[0], first_task[1])
    
