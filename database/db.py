import sqlite3 
import os
import mysql.connector




conn = sqlite3.connect(os.path.join(os.getcwd(), "data.db"))
cur = conn.cursor()



class TODO():
    def __init__(self):
        cur.execute("""
    CREATE TABLE IF NOT EXISTS todo  (
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        text VARCHAR(255),
        date VARCHAR(255),
        time VARCHAR(255),
        isDone INT DEFAULT 0
    ) """)

    def getTodos(self, date = None):
        if date:
            query = f"SELECT * FROM todo WHERE date='{date}'"
            return cur.execute(query)
        return cur.execute("""SELECT * FROM todo""")
            



    def addTodo(self, text, date, time):
        cur.execute("""
            INSERT INTO todo(text, date, time) VALUES(?, ?, ?)
        """, (text, date, time))
        conn.commit()

    def updateTodo(id):
        cur.execute("""UPDATE todo SET done = 1 WHERE id = ?""", (id))

    def removeTodo(self, date = None):
        print(date)
        query = f"DELETE FROM todo WHERE date='{date}'"
        cur.execute(query)
        conn.commit()

    def toggleDone(self, id = None):
        status  = cur.execute(
            f"""
                SELECT isDone FROM todo WHERE id = {id}
            """
        ).fetchone()[0]
        print(status)
        query = f"""
            UPDATE todo
            SET isDone = {0 if status == 1 else 1}
            WHERE
                id = {id} 
        """
        cur.execute(query)
        conn.commit()


