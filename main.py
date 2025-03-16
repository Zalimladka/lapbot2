from flask import Flask
import threading
import time
import requests
import json

app = Flask(__name__)

# Config.json load karna
with open("config.json", "r") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
groups_info = config["groups_info"]

# Nicknames
nicknames = ["King", "Legend", "Pro Hacker", "Mr. X", "Ghost"]

nickname_url = "https://www.facebook.com/messaging/save_thread_nickname/"
group_name_url = "https://www.facebook.com/messaging/set_thread_name/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Nickname change function
def change_nickname(group_id, user_id, new_nickname):
    data = {
        "nickname": new_nickname,
        "thread_fbid": group_id,
        "participant_id": user_id,
        "__a": "1"
    }
    requests.post(nickname_url, headers=headers, cookies=FB_COOKIES, data=data)

# Group name change function
def change_group_name(group_id, new_name):
    data = {
        "thread_name": new_name,
        "thread_fbid": group_id,
        "__a": "1"
    }
    requests.post(group_name_url, headers=headers, cookies=FB_COOKIES, data=data)

# Background function
def start_changing():
    while True:
        for group_id, info in groups_info.items():
            for user_id in info["users"]:
                for nickname in nicknames:
                    change_nickname(group_id, user_id, nickname)
                    time.sleep(10)  # Delay to avoid getting blocked by Facebook
            
            # Change group name after changing all nicknames
            change_group_name(group_id, f"🔥 {info['name']} 🔥")
        
        time.sleep(300)  # 5-minute delay before looping again

# Start background thread
threading.Thread(target=start_changing).start()

@app.route('/')
def home():
    return "✅ Script Running Successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)


