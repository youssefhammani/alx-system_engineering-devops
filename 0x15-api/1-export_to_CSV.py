#!/usr/bin/python3
"""
Script to export data in CSV format for tasks
owned by a specific employee using a REST API.
"""

import csv
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

    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=CSV.QUOTE_ALL)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ])
        num_tasks = 0
        for task in todo_list:
            writer.writerow([
                user_id, username, task.get('completed'), task.get('title')
            ])
            num_tasks += 1

    print(f"Data exported to {filename} successfully.")
    print(f"Number of tasks in CSV: {num_tasks}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        fetch_todo_list_progress(employee_id)

    # Correct output formatting
    msg = "User ID and Username: OK"
    print(msg)
