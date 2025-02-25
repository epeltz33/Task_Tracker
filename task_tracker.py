import json
import os
import sys
import argparse
from datetime import datetime

# Constants
TASKS_FILE = "tasks.json"
STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in_progress"
STATUS_DONE = "done"
MAX_TITLE_LENGTH = 100

# Functions to interact with the JSON file
def load_tasks():
    """Load tasks from the JSON file"""
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {TASKS_FILE} is corrupted.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

# Task operations
def add_task(title):
    """Add a new task"""
    if not title:
        print("Error: Task title cannot be empty.")
        return

    if len(title) > MAX_TITLE_LENGTH:
        print(f"Error: Task title is too long (max {MAX_TITLE_LENGTH} characters).")
        return

    tasks = load_tasks()

    # Generate a new unique ID
    task_id = 1
    if tasks:
        task_id = max(task["id"] for task in tasks) + 1

    now = datetime.now().isoformat()
    new_task = {
        "id": task_id,
        "title": title,
        "status": STATUS_TODO,
        "created_at": now,
        "updated_at": now
    }

    tasks.append(new_task)
    if save_tasks(tasks):
        print(f"Task '{title}' added with ID {task_id}.")
    else:
        print("Failed to add task.")

def update_task(task_id, title):
    """Update a task's title"""
    if not title:
        print("Error: Task title cannot be empty.")
        return

    if len(title) > MAX_TITLE_LENGTH:
        print(f"Error: Task title is too long (max {MAX_TITLE_LENGTH} characters).")
        return

    tasks = load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = title
            task["updated_at"] = datetime.now().isoformat()
            task_found = True
            break

    if task_found:
        if save_tasks(tasks):
            print(f"Task {task_id} updated.")
        else:
            print("Failed to update task.")
    else:
        print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    initial_count = len(tasks)

    tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) < initial_count:
        if save_tasks(tasks):
            print(f"Task {task_id} deleted.")
        else:
            print("Failed to delete task.")
    else:
        print(f"Task with ID {task_id} not found.")

def update_status(task_id, status):
    """Update a task's status"""
    if status not in [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]:
        print(f"Error: Invalid status '{status}'.")
        return

    tasks = load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            task_found = True
            break

    if task_found:
        if save_tasks(tasks):
            print(f"Task {task_id} marked as {status}.")
        else:
            print("Failed to update task status.")
    else:
        print(f"Task with ID {task_id} not found.")

def list_tasks(status=None):
    """List tasks, optionally filtered by status"""
    tasks = load_tasks()

    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    print("\nID | Status | Title")
    print("-" * 50)
    for task in filtered_tasks:
        status_display = task['status'].replace('_', ' ')
        print(f"{task['id']} | {status_display} | {task['title']}")
    print()

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Simple Task Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    # Update task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("title", help="New task description")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Mark as in progress
    progress_parser = subparsers.add_parser("progress", help="Mark a task as in progress")
    progress_parser.add_argument("id", type=int, help="Task ID")

    # Mark as done
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", action="store_true", help="List all tasks")
    list_parser.add_argument("--done", action="store_true", help="List completed tasks")
    list_parser.add_argument("--todo", action="store_true", help="List tasks not done")
    list_parser.add_argument("--progress", action="store_true", help="List tasks in progress")

    # Parse arguments
    args = parser.parse_args()

    # Execute the appropriate command
    if args.command == "add":
        add_task(args.title)
    elif args.command == "update":
        update_task(args.id, args.title)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "progress":
        update_status(args.id, STATUS_IN_PROGRESS)
    elif args.command == "done":
        update_status(args.id, STATUS_DONE)
    elif args.command == "list":
        if args.done:
            list_tasks(STATUS_DONE)
        elif args.todo:
            list_tasks(STATUS_TODO)
        elif args.progress:
            list_tasks(STATUS_IN_PROGRESS)
        else:  # --all or no flag
            list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()