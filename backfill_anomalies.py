import sqlite3

DB_FILE = "database.db"

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    cur.execute("""
                   SELECT * FROM students
                   """)
    rows = cur.fetchall()
    for r in rows:
        print(r)
