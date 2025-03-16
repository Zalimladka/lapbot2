import requests
import time
import json

# Config file se data load karna
with open("config.json", "r") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
groups_info = config["groups_info"]

# Nicknames to cycle
nicknames = ["King", "Legend", "Pro Hacker", "Mr. X", "Ghost"]

# Facebook endpoints
nickname_url = "https://www.facebook.com/messaging/save_thread_nickname/"
group_name_url = "https://www.facebook.com/messaging/set_thread_name/"

# Headers to mimic browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Function to change nickname
def change_nickname(group_id, user_id, new_nickname):
    data = {
        "nickname": new_nickname,
        "thread_fbid": group_id,
        "participant_id": user_id,
        "__a": "1"
    }
    response = requests.post(nickname_url, headers=headers, cookies=FB_COOKIES, data=data)
    if response.status_code == 200:
        print(f"✅ {user_id} ka nickname {new_nickname} set ho gaya!")
    else:
        print("❌ Nickname change failed!")

# Function to change group name
def change_group_name(group_id, new_name):
    data = {
        "thread_name": new_name,
        "thread_fbid": group_id,
        "__a": "1"
    }
    response = requests.post(group_name_url, headers=headers, cookies=FB_COOKIES, data=data)
    if response.status_code == 200:
        print(f"✅ Group name changed to: {new_name}")
    else:
        print("❌ Group name change failed!")

# Main loop to change nicknames and group names every 5 minutes
while True:
    for group_id, info in groups_info.items():
        for user_id in info["users"]:
            for nickname in nicknames:
                change_nickname(group_id, user_id, nickname)
                time.sleep(60)  # Sleep to avoid rate limiting
        change_group_name(group_id, f"🔥 {info['name']} 🔥")
    time.sleep(300)  # Sleep for 5 minutes before starting the loop again
