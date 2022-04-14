import datetime
import sqlite3 
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(".local.env")
print(os.environ["DATABASE_USER"])



conn = mysql.connector.connect(
  host="127.0.0.1",
  user=os.environ["DATABASE_USER"],
  password=os.environ["DATABASE_PASSWORD"],
  database = os.environ["DATABASE_NAME"]
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
        try:
            if date:
                query = f"SELECT * FROM todo WHERE date='{date}'"
                cur.execute(query)
                return [ todo for todo in cur]
            return []
        except:
            print("Something went wrong while getting the records")
                



    def addTodo(self, text, date, time):
        try:
            cur.execute(f"""
                INSERT INTO todo(text, date, time) VALUES('{text}', '{date}', '{time}')
            """)

            conn.commit()
        except:
            print("Something went wrong while inserting the records")



    def updateTodo(id):
        try:
            cur.execute("""UPDATE todo SET done = 1 WHERE id = ?""", (id))
            conn.commit()
        except:
            print("Something went wrong while updating the records")

    def removeTodo(self, date = None):
        print(date)
        query = f"DELETE FROM todo WHERE date='{date}'"
        cur.execute(query)
        conn.commit()

    def toggleDone(self, id = None):
        try:
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
        except:
            print("Someting went wrong while toggling")


