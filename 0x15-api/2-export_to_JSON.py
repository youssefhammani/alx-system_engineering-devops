#!/usr/bin/python3
"""
Script to export data in JSON format for tasks
owned by a specific employee using a REST API.
"""

import json
import requests
from sys import argv


def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for the given employee ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_info = response.json()

    if "id" not in employee_info:
        print("Employee not found.")
        return

    user_id = employee_info.get("id")
    username = employee_info.get("username")

    print(f"User ID: {user_id} / Username: {username}")

    todo_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    tasks = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        for task in todo_list
    ]

    filename = f"{user_id}.json"
    with open(filename, 'w') as file:
        json.dump({str(user_id): tasks}, file, indent=4)

    print(f"Data exported to {filename} successfully.")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(argv[1])
        fetch_todo_list_progress(employee_id)
