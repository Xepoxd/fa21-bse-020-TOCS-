import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database='exampledb',
        user='user',
        password='password'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS blog')
    cur.execute('CREATE TABLE blog (id SERIAL PRIMARY KEY, title VARCHAR (255))')
    cur.executemany('INSERT INTO blog (title) VALUES (%s)', [('Blog post 1',), ('Blog post 2',)])
    cur.execute('SELECT title FROM blog')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
