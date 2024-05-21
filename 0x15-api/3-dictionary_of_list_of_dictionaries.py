#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

if __name__ == "__main__":

    import requests
    import sys
    import json

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    allTodos = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDic = {"username": user.get('username'),
                           "task": task.get('title'),
                           "completed": task.get('completed')}
                taskList.append(taskDic)
        allTodos[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(allTodos, f)
