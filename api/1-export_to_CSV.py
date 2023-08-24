#!/usr/bin/python3
"""program that copeis all tasks in a json file"""
import csv
import requests
import sys


def export_employee_tasks_to_csv(employee_id, employee_name, tasks_data):
    csv_file_path = f"{employee_id}.csv"

    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write tasks data
        for task in tasks_data:
            task_completed = "True" if task["completed"] else "False"
            writer.writerow([employee_id, employee_name,
                            task_completed, task["title"]])


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

    export_employee_tasks_to_csv(employee_id, employee_name, tasks_data)


if __name__ == "__main__":
    main()
