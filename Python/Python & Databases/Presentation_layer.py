# Fernando Parra
# Task List
# 11/08/2024
# Program that allows to manage a task list that is stored in a database
# Presentation layer (Interface)

from business import *
from database import *

def main():
    print("Task List")
    command_menu = ("\nCOMMAND MENU\n"
                    "view     - View pending tasks\n"
                    "history  - View completed tasks\n"
                    "add      - Add a task\n"
                    "complete - Complete a task\n"
                    "delete   - Delete a task\n"
                    "exit     - Exit program")
    print(command_menu)
    active = True
    while active:
        database_list = retriever()
        command = input("\nCommand: ")
        while active:
            match command:
                case "view":
                    display_view(database_list)
                    break
                case "history":
                    display_history(database_list)
                    break
                case "add":
                    add(prompt_addition())
                    break
                case "complete":
                    update(prompt_completion(database_list))
                    break
                case "delete":
                    delete(prompt_deletion(database_list))
                    break
                case "exit":
                    print("\nBye!")
                    active = False
                case Exception as e:
                    print(f"\nInvalid command: ({e})")
                    print(command_menu)
                    command = input("\nCommand: ")

if __name__ == '__main__':
    main()
