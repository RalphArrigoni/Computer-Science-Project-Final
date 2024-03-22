from flask import Flask, render_template, request, session
import sqlite3
import os
app = Flask(__name__)

fHalf = str('<head> <style> .funky {border-top-color : 1px solid #0f0010} .grid-container {   display: grid;   grid-template-columns:')

sHalf = str(';} .grid-item {   background-color: rgba(100, 100, 80, 0.8); border: 1px solid rgba(0, 0, 0, 0.8);  padding: 20px;   font-size: 30px;   text-align: center; </style> </head> <body> <div class=\"grid-container\">')

app.secret_key = os.urandom(16)
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
    else:
        username = "not logged in"
    return render_template('Index.html',username=username)

@app.route('/login')
def login():
    return render_template ('Login.html')

@app.route('/Generate Maze')
def MazeMk3():
    return render_template ('MazeMk3.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return render_template ('Index.html')

@app.route('/signup')
def signup():
    return render_template('Signup.html')


@app.route('/maze')
def maze():
    return render_template('Maze.html')



@app.route('/select', methods=['POST'])
def select():
    con=sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute(""" SELECT * FROM login
                    WHERE username = ? AND password = ?""",
                    (request.form['username'], request.form['password']))
    rows = cur.fetchall()
    if len(rows) == 1:
        session['username'] = request.form['username']
        return render_template('Index.html')
    else:
        return "Username and password not found"

@app.route('/insert', methods=['POST'])
def insert():
    con=sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO login (username, password)
    VALUES (?, ?)
    """,(request.form['username'], request.form['password']))
    con.commit()
    con.close()
    return render_template ('Login.html')


@app.route('/tbl')
def db():
    con=sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE login
    (
    username VARCHAR(20) NOT NULL PRIMARY KEY,
    password VARCHAR(20) NOT NULL
    )
    """)
    return "database created!"
