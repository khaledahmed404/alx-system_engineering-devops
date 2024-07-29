#!/usr/bin/python3
"""
Give out the information for given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def print_details_csv(user_id):
    """
    Print out the todo list information for a given employee ID
    """
    res = \
        requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    res = res.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user_todo = []
    for todo in todos:
        if todo.get("userId") == user_id:
            user_todo.append(todo)
    ans = []

    for user in user_todo:
        temp = [user_id, res.get("username"), user.get("completed"),
                user.get("title")]
        ans.append(temp)

    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in ans:
            writer.writerow(row)


if __name__ == "__main__":
    print_details_csv(int(sys.argv[1]))
