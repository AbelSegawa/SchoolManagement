from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "school.db")
os.makedirs(DB_DIR, exist_ok=True)

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)
    conn.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin123', 'admin')")
    conn.commit()
    conn.close()
    print("DB ready at:", DB_PATH)

LOGIN_HTML = """<!doctype html><html><head><title>Login</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;background:#f0f2f5}.box{background:white;padding:30px;border-radius:10px;box-shadow:0 2px 10px rgba(0,0,0,0.1);width:300px}input{width:100%;padding:10px;margin:8px 0;border:1px solid #ccc;border-radius:5px}button{width:100%;padding:10px;background:#1877f2;color:white;border:none;border-radius:5px} .error{color:red}</style></head><body><div class="box"><h2>School Login</h2><form method="post"><input name="username" placeholder="Username" required><input name="password" type="password" placeholder="Password" required><button>Login</button></form>{% if error %}<p class="error">{{error}}</p>{% endif %}</div></body></html>"""

DASHBOARD_HTML = """<!doctype html><html><head><title>Dashboard</title><style>body{font-family:Arial;padding:40px;background:#f0f2f5}.box{background:white;padding:30px;border-radius:10px}a{color:#1877f2}</style></head><body><div class="box"><h2>Welcome {{username}}!</h2><p>Role: {{role}}</p><a href="/logout">Logout</a></div></body></html>"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
        conn.close()
        if user:
            session["user"] = dict(user)
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"
    return render_template_string(LOGIN_HTML, error=error)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    user = session["user"]
    return render_template_string(DASHBOARD_HTML, username=user["username"], role=user["role"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
