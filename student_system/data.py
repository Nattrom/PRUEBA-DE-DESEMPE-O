import json #To work with JSON files
import os  #To check if file exists

#File where students will be stored
FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return [] #return empty list if no file

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)