from flask import Flask, render_template, request, jsonify, make_respons, session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
