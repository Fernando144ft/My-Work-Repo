# Fernando Parra
# Data tier
# 11/08/2024
# Data retrival layer, databases or traditional data files.

import sqlite3, business
from contextlib import *

connection = sqlite3.connect('task_list_db.sqlite')
connection.row_factory = sqlite3.Row

def retriever(): # Return a list of task objects
    get_all = '''SELECT
                    TaskID,
                    description,
                    completed
                FROM Task'''

    with closing(connection.cursor()) as c:
        c.execute(get_all)
        fetched_list = c.fetchall()
        objects_list = []
        for column in fetched_list:
            task_object = business.Task(column['description'],
                                        column['completed'],
                                        column['taskID'])
            objects_list.append(task_object)
        return objects_list

def add(task_object):
    with closing(connection.cursor()) as c:
        c.executescript(f"""
                BEGIN;
                INSERT INTO Task (description, completed)
                VALUES ('{task_object.description}', {task_object.completed});
                COMMIT;""")

def update(selection):
    try:
        with (closing(connection.cursor()) as c):
            c.executescript(f"""
                            BEGIN;
                            UPDATE Task
                            SET completed = 1
                            WHERE TaskID = '{selection}';
                            COMMIT;
                            """)
    except sqlite3.OperationalError as e:
        print(e)

def delete(selection):
    try:
        with closing(connection.cursor()) as c:
            c.executescript(f"""
                            BEGIN;
                            DELETE
                            FROM Task
                            WHERE TaskID = '{selection}';
                            COMMIT;
                            """)
    except sqlite3.OperationalError as e:
        print(f"Invalid: {e}")
