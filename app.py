from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.close()
    return "Hello DevOps Assignment - CI/CD Pipeline Working"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
