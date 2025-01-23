import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Task Tracker - Manage your tasks efficiently')
    # subparser for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Task description')

    #update command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('description', type=str, help='New task description')

    #delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help='Task ID')

    # Status command
    status_parser = subparsers.add_parser('status', help='Get status of a task')
    status_parser.add_argument('id', type=int, help='Task ID')
    status_parser.add_argument('description', type=str, help='Status of a task')

    # list command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--filter', choices=['all', 'in_progress', 'not_started' 'done'],
                             default='all', help='Filter tasks by status')

    return parser






