# Tasks CLI
> Un administrador de tareas simple por línea de comandos para poder organizar tareas personales.

## Características
- Crear tareas
- Borrar tareas
- Marcar y desmarcar tareas como completadas
- Persistencia con JSON automática
- CLI interactivo e intuitivo

## Tecnologías
- Python 3.14
- JSON
- Unittest

## Estructura

```
tasks-cli/
├── data/
│   └── data.json              --> Archivo JSON de persistencia de las tareas
├── src/
│   ├── __init__.py
│   ├── main.py                --> Desde donde se ejecuta la aplicación
│   ├── task.py                --> Clase de cada tarea con sus propiedades
│   └── task_manager.py        --> Clase del manager de tareas, gestiona todas las operaciones 
├── tests/
│   ├── data_test.json         --> Archivo JSON de persistencia para ejecutar los tests
│   └── task_manager_tests.py  --> Tests de la aplicación
├── .gitignore
└── README.md
```


## Arquitectura

- La aplicación está dividida en 3 componentes principales:
1. `main.py` inicia el CLI.
2. `TaskManager` contiene la lógica de negocio.
3. `data.json` almacena y persiste las tareas.

```
TaskManager
│
├── Maneja los objetos tarea: crear, borrar, completar
├── Recupera tareas del JSON
└── Persiste tareas al JSON
```

## Testing
- Los tests unitarios cubren todas las acciones básicas (creación, borrado, completado) de tareas, lógica interna como búsqueda o generación correcta de IDs, también casos límite y persistencia.

## Cómo ejecutar
#### Requerimientos
Python 3.12+

#### Ejecutar el proyecto
```python -m src.main```

#### Ejecutar los tests
```python -m tests.test_task_manager.py```

## Mejoras futuras
- Modificación de tareas
- Incorporación de fechas límite de tareas
- Búsqueda por nombre de tareas
- Persistencia con SQLite
- Refactorizar la app para separar lógica de negocio de la CLI
