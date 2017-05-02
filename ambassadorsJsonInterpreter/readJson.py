"""
Kurt Lewis
Reading data from .json file.
Remember that the data I get direct from the database is gross. I probably need to put it in an array and add comma delimiters.
I did that using this direct from the python CLI
file = open("memberInfo.json", 'r')
content = file.read()
file.close()
content = content.close("}\n{" "},\n{")
file = open("memberInfo2.json", 'w')
file.write(content)
file.close()
"""
import json

print("Name,Email,Minutes")

with open("memberInfo.json", 'r') as data_file:
    data = json.loads(data_file.read())
    for idData in data:
        print(str(idData['profile']['firstName'] + " " + str(idData['profile']['lastName'])), end=",")
        print(str(idData['email']), end=",")
        print(str(idData["service"]), end=",")
        print()

#print("File complete.")