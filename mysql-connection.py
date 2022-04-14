import datetime
import sqlite3 
import os
import mysql.connector




conn = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="12345678",
  database = "test"
)
cur = conn.cursor()



class TODO():
    def __init__(self):
      try:
          cur.execute("""
      CREATE TABLE IF NOT EXISTS todo  (
          id INT AUTO_INCREMENT PRIMARY KEY,
          text VARCHAR(255),
          date VARCHAR(255),
          time VARCHAR(255),
          isDone INT DEFAULT 0
      ) """)
      except:
        print("Something went wrong")

    def getTodos(self, date = None):
        if date:
            query = f"SELECT * FROM todo WHERE date='{date}'"
            cur.execute(query)
            return [ todo for todo in cur]
        return []
            



    def addTodo(self, text, date, time):
        cur.execute(f"""
            INSERT INTO todo(text, date, time) VALUES('{text}', '{date}', '{time}')
        """)

        conn.commit()

    def updateTodo(id):
        cur.execute("""UPDATE todo SET done = 1 WHERE id = ?""", (id))
        conn.commit()

    def removeTodo(self, date = None):
        print(date)
        query = f"DELETE FROM todo WHERE date='{date}'"
        cur.execute(query)
        conn.commit()

    def toggleDone(self, id = None):
        cur.execute(
            f"""
                SELECT isDone FROM todo WHERE id = {id}
            """
        )
        status = cur.fetchone()[0]
        print(status)
        query = f"""
            UPDATE todo
            SET isDone = {0 if status == 1 else 1}
            WHERE
                id = {id} 
        """
        
        cur.execute(query)
        conn.commit()



todo = TODO()

todo.toggleDone(id = 1)
print(todo.getTodos(date = datetime.datetime.now().strftime("%d/%m/%y")))