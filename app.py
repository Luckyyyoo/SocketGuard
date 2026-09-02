import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Dynamically locate alerts.json in the exact same folder as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALERTS_FILE = os.path.join(BASE_DIR, "alerts.json")


def get_alerts():
    try:
        with open(ALERTS_FILE, "r") as file:
            alerts = json.load(file)
    except Exception as e:
        print(f"Error loading alerts.json: {e}")
        alerts = []
    return alerts


@app.route("/")
def home():
    alerts = get_alerts()
    return render_template("index.html", alerts=alerts)


if __name__ == "__main__":
    print("SocketGuard Dashboard is starting...")
    print("Open http://127.0.0.1:5000/ in your browser")
    
    app.run(host="0.0.0.0", port=5000, debug=True)
