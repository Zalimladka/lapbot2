import json
import requests
from flask import Flask, jsonify
from fake_useragent import UserAgent

app = Flask(__name__)
ua = UserAgent()

with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
GROUPS = config["groups_info"]

def check_facebook_cookies():
    headers = {
        "User-Agent": ua.random,
        "Referer": "https://m.facebook.com",
        "Origin": "https://m.facebook.com"
    }
    response = requests.get("https://m.facebook.com", headers=headers, cookies=FB_COOKIES)
    if "login" in response.url:
        return False
    return True

@app.route('/')
def index():
    if not check_facebook_cookies():
        return jsonify({"status": "❌ Invalid XS Token"})

    return jsonify({"status": "✅ Bot Ready for Nickname Change"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
