from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.secret_key = "admin123"

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        return "Login Successful"

    return "Invalid Credentials"

app.run(debug=True)



SECURE CODE 
from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Invalid Input"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=? AND password=?"

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    if user:
        return "Login Successful"

    return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=False)
