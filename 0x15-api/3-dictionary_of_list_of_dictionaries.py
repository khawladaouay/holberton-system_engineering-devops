#!/usr/bin/python3
"""returns list dictionaries."""
from json import dump
from requests import get

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = get('{}/users'.format(url)).json()
    target = get('{}/todos'.format(url)).json()
    data = {}
    for u in user:
        employeeName = u.get('username')
        todo = get(
            "{}/users/{}/todos".format(url, u.get('id'))).json()
        row = []
        for elem in todo:
            if elem.get('userId') == u.get('id'):
                dict = {
                    "username": employeeName,
                    "task": elem.get('title'),
                    "completed": elem.get('completed')
                }
                row.append(dict)
            data[u.get('id')] = row

    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        file.write(dump(data))
