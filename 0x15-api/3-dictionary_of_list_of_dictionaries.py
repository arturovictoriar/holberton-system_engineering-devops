#!/usr/bin/python3
"""
    Uses the fake API to get all employers and their todos and export as json
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_employ = "https://jsonplaceholder.typicode.com/users"
    r_employs = requests.get(url_employ).json()
    report = {}
    for employ in r_employs:
        id_em = employ.get("id")
        url_todos = url_employ + "/{}/todos".format(id_em)
        r_todos = requests.get(url_todos).json()
        username = employ.get("username")
        total_num_task = r_todos
        list_dict_report = []
        for task in total_num_task:
            id_report = {}
            id_report["username"] = str(username)
            id_report["completed"] = task.get("completed")
            id_report["task"] = str(task.get("title"))
            list_dict_report.append(id_report)
        report[id_em] = list_dict_report
    with open("todo_all_employees.json", "w") as fjson:
        fjson.write(json.dumps(report))
