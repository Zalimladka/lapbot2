import json
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "✅ Bot Running Successfully!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
