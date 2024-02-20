#!/usr/bin/python3
"""Python script to retrieve employee TODO list progress from a REST API."""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    try:
        user_response = requests.get(url_user)
        todos_response = requests.get(url_todos)
        user_data = user_response.json()
        todos_data = todos_response.json()
        
        if user_response.status_code != 200:
            print("User data request failed")
            sys.exit(1)
        if todos_response.status_code != 200:
            print("Todos data request failed")
            sys.exit(1)

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))

    except Exception as e:
        print("Error:", e)
