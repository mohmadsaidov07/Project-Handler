import psycopg2
from psycopg2.extras import NamedTupleCursor
from typing import List
from classes import Task, Developer, Project, Note


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


def run_sql(sql_request, cursorF=None, isFetching=True):
    conn = connect_sql()
    cursor = conn.cursor(cursor_factory=cursorF)
    cursor.execute(sql_request)
    conn.commit()
    if isFetching:
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    cursor.close()
    conn.close()
    return "Done"


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
        """
        SELECT table_name FROM information_schema.tables 
        WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name;"""
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


def get_data(sql_request: str) -> List:
    conn = connect_sql()
    all_obj = []
    cursor = conn.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute(sql_request)
    rows = cursor.fetchall()

    for row in rows:
        all_obj.append(find_table(sql_request)(**row._asdict()))
    cursor.close()
    conn.close()
    return all_obj


if __name__ == "__main__":
    print(get_data("SELECT * FROM tasks;"))
