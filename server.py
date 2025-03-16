from flask import Flask
import threading
import time
import json
import requests
from http.cookies import SimpleCookie

app = Flask(__name__)

# Load config.json
with open("config.json", "r") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
groups_info = config["groups_info"]

# Nicknames
nicknames = ["King", "Legend", "Pro Hacker", "Mr. X", "Ghost"]

# Facebook Endpoints
nickname_url = "https://www.facebook.com/messaging/save_thread_nickname/"
group_name_url = "https://www.facebook.com/messaging/set_thread_name/"

# Convert cookies to dictionary
cookie = SimpleCookie()
cookie.load(FB_COOKIES)
cookies = {key: morsel.value for key, morsel in cookie.items()}

# Facebook Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Change Nickname
def change_nickname(group_id, user_id, new_nickname):
    data = {
        "nickname": new_nickname,
        "thread_fbid": group_id,
        "participant_id": user_id,
        "__a": "1"
    }
    response = requests.post(nickname_url, cookies=cookies, data=data, headers=headers)
    if response.status_code == 200:
        print(f"✅ Nickname Changed: {user_id} -> {new_nickname}")
    else:
        print("❌ Nickname Change Failed!")

# Change Group Name
def change_group_name(group_id, new_name):
    data = {
        "thread_name": new_name,
        "thread_fbid": group_id,
        "__a": "1"
    }
    response = requests.post(group_name_url, cookies=cookies, data=data, headers=headers)
    if response.status_code == 200:
        print(f"✅ Group Name Changed: {new_name}")
    else:
        print("❌ Group Name Change Failed!")

# Loop to update every 5 mins
def loop_script():
    while True:
        for group_id, info in groups_info.items():
            for user_id in info["users"]:
                for nickname in nicknames:
                    change_nickname(group_id, user_id, nickname)
                    time.sleep(60)
            change_group_name(group_id, f"🔥 {info['name']} 🔥")
        time.sleep(300)

@app.route('/')
def home():
    return "✅ Bot is Running!"

# Background Thread
threading.Thread(target=loop_script, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
