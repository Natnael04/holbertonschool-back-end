#!/usr/bin/python3
"""program that copeis all tasks in a json file"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """get employee information based on id"""
    base_url = "https://jsonplaceholder.typicode.com"


    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]


    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()


    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])


    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
