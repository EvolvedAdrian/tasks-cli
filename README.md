<sub>[Leer en español](README.es.md)</sub>

# Tasks CLI
> A simple command-line task manager to easily organize personal tasks.

## Features
- Create tasks
- Delete tasks
- Mark and unmark tasks as completed
- Automatic persistence with JSON
- Interactive and intuitive CLI

## Technologies
- Python 3.14
- JSON
- Unittest

## Structure

```
tasks-cli/
├── data/
│   └── data.json              --> JSON file for task persistence
├── src/
│   ├── __init__.py
│   ├── main.py                --> Where the application is run from
│   ├── task.py                --> Class for each task with its properties
│   └── task_manager.py        --> Task manager class, handles all operations
├── tests/
│   ├── data_test.json         --> JSON file for persistence used to run the tests
│   └── task_manager_tests.py  --> Application tests
├── .gitignore
└── README.md
```


## Architecture

- The application is divided into 3 main components:
1. `main.py` starts the CLI.
2. `TaskManager` contains the business logic.
3. `data.json` stores and persists the tasks.

```
TaskManager
│
├── Handles task objects: create, delete, complete
├── Retrieves tasks from JSON
└── Persists tasks to JSON
```

## Testing
- The unit tests cover all basic task actions (creation, deletion, completion), internal logic such as search or correct ID generation, as well as edge cases and persistence.

## How to run
#### Requirements
Python 3.12+

#### Run the project
```python -m src.main```

#### Run the tests
```python -m tests.test_task_manager.py```

## Future improvements
- Task editing
- Adding task due dates
- Search by task name
- Persistence with SQLite
- Refactor the app to separate business logic from the CLI
