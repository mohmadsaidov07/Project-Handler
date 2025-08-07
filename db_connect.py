import psycopg2
from psycopg2.extras import NamedTupleCursor
from typing import List, Optional, Dict, Literal, Tuple
from classes import Priority, Task, Developer, Project, Note


def connect_sql():
    try:
        conn = psycopg2.connect(
            database="managment_sys",
            user="postgres",
            password="mohmad2007",
            host="localhost",
            port=5433,
        )

    except psycopg2.Error as err:
        print(f"Error {err}")

    return conn


def find_table(sql_request):
    conn = connect_sql()

    letters = "qwertyuiopasdfghjklzxcvbnm "
    symbolLess_request = []
    for letter in list(sql_request):
        if letter.lower() in letters:
            symbolLess_request.append(letter)
    symbolLess_request = "".join(symbolLess_request).split()

    table_cursor = conn.cursor()
    table_cursor.execute(
        "SELECT table_name FROM information_schema.tables \
        WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema')\
        ORDER BY table_schema, table_name;"
    )
    tables = table_cursor.fetchall()
    table_names = [name[0] for name in tables]
    curr_table = [word for word in symbolLess_request if word in table_names][0]
    table_class = {
        "developers": Developer,
        "projects": Project,
        "tasks": Task,
        "notes": Note,
    }

    return table_class[curr_table]


# FIXME: don't forget to add async support for database operations in the future
def get_data(sql_request: str) -> List:
    conn = connect_sql()
    all_tasks = []
    cursor = conn.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(sql_request)
    rows = cursor.fetchall()

    for row in rows:
        all_tasks.append(find_table(sql_request)(**row._asdict()))
    cursor.close()
    conn.close()
    return all_tasks


if __name__ == "__main__":
    get_data("SELECT * FROM tasks")
