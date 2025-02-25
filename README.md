# Command Line Task Tracker

A lightweight, file-based task management system that runs directly from your command line. This simple yet powerful tool helps you organize your tasks without any external dependencies or complicated setup.


## Features

- ✅ Add, update, and delete tasks
- ⏳ Mark tasks as "in progress" or "done"
- 📋 List all tasks or filter by status
- 💾 Persistent storage using JSON
- 🛠️ No external dependencies
- 🔒 Error handling and validation built-in

## Installation

No installation required beyond Python! Simply download the script and you're ready to go.

```bash
# Clone this repository
git clone https://github.com/username/task-tracker.git

# Navigate to the repository directory
cd task-tracker

# Run the script (examples below)
python task_tracker.py add "My first task"
```

## Requirements

- Python 3.6+
- No external libraries required

## Usage Examples

### Adding a task

```bash
python task_tracker.py add "Complete project proposal"
# Output: Task 'Complete project proposal' added with ID 1.
```

### Updating a task

```bash
python task_tracker.py update 1 "Revised project proposal"
# Output: Task 1 updated.
```

### Marking a task as in progress

```bash
python task_tracker.py progress 1
# Output: Task 1 marked as in_progress.
```

### Marking a task as done

```bash
python task_tracker.py done 1
# Output: Task 1 marked as done.
```

### Deleting a task

```bash
python task_tracker.py delete 1
# Output: Task 1 deleted.
```

### Listing tasks

List all tasks:
```bash
python task_tracker.py list
```

List only completed tasks:
```bash
python task_tracker.py list --done
```

List only todo tasks:
```bash
python task_tracker.py list --todo
```

List only in-progress tasks:
```bash
python task_tracker.py list --progress
```

## Command Reference

| Command | Description | Format |
|---------|-------------|--------|
| `add` | Create a new task | `add "Task title"` |
| `update` | Update an existing task | `update <id> "New title"` |
| `delete` | Remove a task | `delete <id>` |
| `progress` | Mark task as in progress | `progress <id>` |
| `done` | Mark task as completed | `done <id>` |
| `list` | Show all tasks | `list [--all/--done/--todo/--progress]` |

## Sample Output

When listing tasks, you'll see output similar to:

```
ID | Status | Title
--------------------------------------------------
1 | todo | Write documentation
2 | in progress | Implement error handling
3 | done | Create basic structure
```

## Data Storage

All tasks are stored in a `tasks.json` file in the same directory as the script. Each task contains:

- Unique ID
- Title
- Status (todo, in_progress, done)
- Creation timestamp
- Last update timestamp

Example structure:
```json
[
  {
    "id": 1,
    "title": "Complete project proposal",
    "status": "done",
    "created_at": "2025-02-25T15:30:45.123456",
    "updated_at": "2025-02-25T16:45:12.654321"
  }
]
```

## Error Handling

The application includes robust error handling for:
- File I/O operations
- Invalid task IDs
- Empty task titles
- Corrupted JSON data
- Excessive title length

## Extending the Application

This task tracker is designed to be simple but extensible. Some ideas for expansion:
- Add due dates
- Task priorities
- Task categories/tags
- Data export functionality
- Interactive mode

## License

MIT License

Copyright (c) 2025 Eric Peltzman

