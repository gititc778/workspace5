import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "APP_ENV": os.getenv("APP_ENV"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
    }
    return jsonify(data)

@app.route("/liveness")
def liveness():
    return "OK", 200

@app.route("/readiness")
def readiness():
    return "READY", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    app.run(host="0.0.0.0", port=8080)
