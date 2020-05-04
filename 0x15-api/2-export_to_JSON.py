#!/usr/bin/python3
"""
    Uses the fake API to get an employer and export the info in json formater
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    id_em = argv[1]
    url_employ = "https://jsonplaceholder.typicode.com/users/{}".format(id_em)
    url_todos = url_employ + "/todos"
    r_employ = requests.get(url_employ).json()
    r_todos = requests.get(url_todos).json()
    username = r_employ.get("username")
    total_num_task = r_todos
    list_dict_report = []
    for task in total_num_task:
        id_report = {}
        id_report["username"] = str(username)
        id_report["completed"] = task.get("completed")
        id_report["task"] = str(task.get("title"))
        list_dict_report.append(id_report)
    report = {}
    report[id_em] = list_dict_report
    with open("{}.json".format(id_em), "w") as fjson:
        fjson.write(json.dumps(report))
