import json
import os
import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    #file does not exist, no tasks
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task_to_list(tasks, title, priority, due_date):
    """Add task to the list."""
    tasks.append({"title": title, "priority": priority, "due_date": due_date, "completed": False})
    # print(tasks)
    save_tasks(tasks)

def delete_task_from_list(tasks, task_index):
    """Delete task from the list."""
    del tasks[task_index]
    save_tasks(tasks)

def sort_tasks_by_priority(tasks):
    """Sort tasks by priority."""
    return sorted(tasks, key=lambda x: x['priority'])
