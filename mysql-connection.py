import mysql.connector

config = {
  'user': 'root',
  'password': '12345678',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cur = cnx.cursor()

cur.execute( "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


cnx.close()