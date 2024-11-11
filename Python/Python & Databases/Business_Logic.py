# Fernando Parra
# Business Tier
# 11/08/2024
# Stores the business logic and rules of the program
from database import update

class Task:
    def __init__(self, description, completed, ID=int):
        self.description = description
        self.completed = completed
        self.ID = ID

    def __str__(self):
        if self.completed == 1:
            return f"{self.ID}. {self.description} (DONE!)"
        else:
            return f"{self.ID}. {self.description} (NOT DONE!)"

def display_view(db_list): # Print pending Task objects
    for row in db_list:
        if row.completed == 0:
            print(f"{row.ID}. {row.description}")

def display_history(db_list): # Print Task objects with overwritten str function
    for row in db_list:
        print(row)

def prompt_addition(): # Ask user for description to make a Task object
    task_object = Task(description=input("Description: "), completed= 0)
    return task_object

def prompt_completion(db_list): # Ask user for TaskID to update task from the database
    while True:
        try:
            update_selection = int(input("Number: "))
            break
        except ValueError:
            print(f"Invalid: {ValueError}")

    for task in db_list:
        if update_selection == task.ID and task.completed == 1:
            print("Task already completed")
            break
        else:
            continue

    for task in db_list:
        if update_selection != task.ID:
            continue
        else:
            return update_selection

    print(f"Number {update_selection} not found.")
    return update_selection

def prompt_deletion(db_list): # Ask user for TaskID to delete Task row from the database
    while True:
        try:
            delete_selection = int(input("Number: "))
            break
        except ValueError:
            print(f"Invalid: {ValueError}")

    for task in db_list:
        if delete_selection == task.ID:
            return delete_selection
        else:
            continue

    return print(f"Number {delete_selection} not found.")
