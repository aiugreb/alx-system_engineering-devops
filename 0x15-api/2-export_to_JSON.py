#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDic = {"task": task.get('title'),
                       "completed": task.get('completed'),
                       "username": user.json().get('username')}
            taskList.append(taskDic)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
