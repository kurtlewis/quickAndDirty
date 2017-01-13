"""
Kurt Lewis
Reading data from .json file.
"""
import json


with open("memberInfo.json", 'r') as data_file:
    data = json.loads(data_file.read())
    for idData in data['members']:
        print("Name: " + str(idData['profile']['firstName'] + " " + str(idData['profile']['lastName'])))
        print("Minutes: " + str(idData["service"]))

print("File complete.")