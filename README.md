# ⚡ Guardian - System Health Monitor

A real-time system monitoring dashboard that tracks CPU, memory, and disk usage — built with Python, Flask, and JavaScript.

---

## 🖥️ Demo

- Live dashboard with real-time charts updating every 3 seconds
- Automatic alerts when metrics cross safe thresholds
- Full history logging via SQLite database

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, psutil |
| Frontend | JavaScript, Chart.js |
| Database | SQLite |
| Testing | Postman |

---

## 📁 Project Structure
```
SysGuard/
├── app.py               # Flask backend & REST API
├── templates/
│   └── index.html       # Dashboard frontend
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Guardian.git
cd Guardian
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Live dashboard |
| GET | `/api/metrics` | Current CPU, memory, disk stats |
| GET | `/api/history` | Last 50 logged readings from DB |

---

## 🚨 Alert Thresholds

| Metric | Threshold |
|---|---|
| CPU | > 75% |
| Memory | > 80% |
| Disk | > 85% |

---

## 👨‍💻 Author

**Swarup** — Computer Science Student  
Built as a portfolio project targeting Software Developer / Application Engineer / SRE roles.
