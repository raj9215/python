import mysql.connector

from flask import Flask

app = Flask(__name__)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="first_python_db"
    )
    mycursor = mydb.cursor()
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    print(f"Failed to connect to MySQL database: {err}")