#!/usr/bin/python3
"""program that copeis all tasks in a json file"""
import requests
import sys


def get_users_information(employee_id):
    api_url = 'https://jsonplaceholder.typicode.com/users/{employee_Id}'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


def main():
    employee_id = 1
    todo_data = get_users_information(employee_id)

    if todo_data is not None:
        EMPLOYEE_NAME = todo_data.get('EMPLOYEE_NAME')
        NUMBER_OF_DONE_TASKS = todo_data.get('NUMBER_OF_DONE_TASKS')
        TOTAL_NUMBER_OF_TASKS = todo_data.get('TOTAL_NUMBER_OF_TASKS')

        print(
            f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in todo_data:
            if task['completed']:
                print(f"\t{'TASK_TITLE'}")


if __name__ == "__main__":
    main()
