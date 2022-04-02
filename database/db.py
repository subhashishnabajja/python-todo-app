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

    def getTodos(self):
        for row in cur.execute("""SELECT * FROM todo"""):
            print(row)    

    def addTodo(self, id, text, date):
        cur.execute("""
            INSERT INTO todo(id, text, date) VALUES(?, ?, ?)
        """, (id, text, date))
        conn.commit()


