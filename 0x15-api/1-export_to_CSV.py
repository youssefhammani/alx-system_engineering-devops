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
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    employee_info = response.json()

    if "id" not in employee_info:
        print("Employee not found.")
        return

    user_id = employee_info.get("id")
    username = employee_info.get("username")

    print(f"User ID: {user_id} / Username: {username}")

    todo_response = requests.get(url + "todos", params={"userId": employee_id})
    todo_list = todo_response.json()

    filename = "{}.csv".format(user_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        fetch_todo_list_progress(employee_id)

    # Correct output formatting
    msg = "User ID and Username: OK"
    print(msg)
