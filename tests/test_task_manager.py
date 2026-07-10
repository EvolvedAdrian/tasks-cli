"""
Tests file : Arrange --> Act --> Assert
"""

import unittest

from src.task_manager import TaskManager

TEST_FILE = "tests/data_test.json"

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Arrange --> prepare environment before tests
        with open(TEST_FILE, "w") as f:
            f.write("")
        
        self.manager = TaskManager(TEST_FILE)
        self.manager.create_task("Task")
    
    def test_create_task(self):
        self.assertEqual(len(self.manager.task_list), 1)

    def test_get_next_task_id(self):
        # Act --> Get next task_id
        next_task_id = self.manager.get_next_task_id()

        self.assertEqual(next_task_id, 2)
    
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
        unfounded_task_0 = self.manager.find_task(0)
        unfounded_task_2 = self.manager.find_task(2)

        self.assertIsNone(unfounded_task_0)
        self.assertIsNone(unfounded_task_2)






