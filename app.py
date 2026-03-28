from flask import Flask, jsonify, render_template
import psutil
import datetime
import sqlite3

app = Flask(__name__)
DB = "sysguard.db"

# ── Initialize database ───────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu       REAL,
            mem       REAL,
            disk      REAL
        )
    ''')
    conn.commit()
    conn.close()

# ── Save one reading to DB ────────────────────────────────
def save_metrics(timestamp, cpu, mem, disk):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO metrics (timestamp, cpu, mem, disk) VALUES (?, ?, ?, ?)",
        (timestamp, cpu, mem, disk)
    )
    conn.commit()
    conn.close()

# ── Dashboard ─────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")

# ── Live system metrics API ───────────────────────────────
@app.route("/api/metrics")
def get_metrics():
    cpu    = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk   = psutil.disk_usage("/")
    ts     = datetime.datetime.now().strftime("%H:%M:%S")

    save_metrics(ts, cpu, memory.percent, disk.percent)

    data = {
        "timestamp": ts,
        "cpu": {
            "percent": cpu
        },
        "memory": {
            "percent": memory.percent,
            "used_gb": round(memory.used / (1024**3), 2),
            "total_gb": round(memory.total / (1024**3), 2)
        },
        "disk": {
            "percent": disk.percent,
            "used_gb": round(disk.used / (1024**3), 2),
            "total_gb": round(disk.total / (1024**3), 2)
        }
    }
    return jsonify(data)

# ── History API ───────────────────────────────────────────
@app.route("/api/history")
def get_history():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT timestamp, cpu, mem, disk FROM metrics ORDER BY id DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()

    history = [
        {"timestamp": r[0], "cpu": r[1], "memory": r[2], "disk": r[3]}
        for r in rows
    ]
    return jsonify(history)

# ── Run the app ───────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    app.run(debug=True)