#!/usr/bin/python3
"""program that copeis all tasks in a json file"""
import json
import requests
import sys


def export_employee_tasks_to_json(employee_id, employee_name, tasks_data):
    tasks_for_json = []

    for task in tasks_data:
        tasks_for_json.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    json_data = {employee_id: tasks_for_json}
    json_file_path = f"{employee_id}.json"

    with open(json_file_path, mode="w") as file:
        json.dump({employee_id: tasks_for_json}, file, indent=4)

    print(
        f"Tasks for employee {employee_name} exported to {json_file_path} successfully.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["username"]

    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    export_employee_tasks_to_json(employee_id, employee_name, tasks_data)


if __name__ == "__main__":
    main()
