from flask import Flask, render_template, request, redirect, url_for
from database.db import init_db, get_conn

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form['username']
    password = request.form['password']
    # TODO: check user in DB
    return render_template('dashboard.html', user=username)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
