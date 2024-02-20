#!/usr/bin/python3
"""
This module provides a sample implementation
following the specified requirements.
"""

import csv
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'
EMPLOYEE_ID = sys.argv[1]


def fetch_user_tasks(user_id):
    """
    Fetches tasks owned by the specified user ID.
    """
    response = requests.get(f'{API_URL}/todos?userId={user_id}')
    if response.status_code != 200:
        print(f"Failed to fetch tasks for user {user_id}")
        return []
    return response.json()


def export_to_csv(user_id, tasks):
    """
    Exports tasks to a CSV file named USER_ID.csv
    """
    filename = f'{user_id}.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ])
        for task in tasks:
            writer.writerow([
                user_id, task['userId'], str(task['completed']), task['title']
            ])
    print(f"Tasks exported to {filename}")


def main():
    """
    Entry point of the script.
    """
    tasks = fetch_user_tasks(EMPLOYEE_ID)
    export_to_csv(EMPLOYEE_ID, tasks)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py USER_ID")
        sys.exit(1)
    main()
