import sqlite3 
import os


conn = sqlite3.connect(os.path.join(os.getcwd(), "data.db"))
cur = conn.cursor()


class TODO():
    def __init__(self):
        cur.execute("""
    CREATE TABLE IF NOT EXISTS todo  (
        id INT AUTO_INCREMENT PRIMARY KEY,
        text VARCHAR(255),
        date VARCHAR(255),
        isDone INT DEFAULT 0
    ) """)

    def getTodos(self, date = None):
        if date:
            query = f"SELECT * FROM todo WHERE date='{date}'"
            return cur.execute(query)
        return cur.execute("""SELECT * FROM todo""")
            



    def addTodo(self, id, text, date):
        cur.execute("""
            INSERT INTO todo(id, text, date) VALUES(?, ?, ?)
        """, (id, text, date))
        conn.commit()

    def updateTodo(id):
        cur.execute("""UPDATE todo SET done = 1 WHERE id = ?""", (id))

    def removeTodo(self, date = None):
        print(date)
        query = f"DELETE FROM todo WHERE date='{date}'"
        cur.execute(query)
        conn.commit()


