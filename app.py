gs zsfrom flask import Flask, render_template, request, jsonify, make_respons, session
app = Flask(__name__)

@app.route('/productos')
def productos():
import mysql.connector

mydb = mysql.connector.connect(
  host="46.28.42.226",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
