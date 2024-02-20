#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    todo_dict = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = []
        todo_list = requests.get(
                "{}/todos?userId={}".format(url, user_id)
        ).json()

        for task in todo_list:
            task_dict = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            }
            tasks.append(task_dict)

        todo_dict[str(user_id)] = tasks

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(todo_dict, jsonfile)
