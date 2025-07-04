# 🔰 This version is for Render testing without actual token

print("✅ Render deploy working! Bot started successfully.")

# Uncomment below when you're ready with real token and files

"""
import time
import requests
import random

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()

def read_lines(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def change_nickname(token, convo_id, user_id, nickname):
    url = f"https://graph.facebook.com/{convo_id}/participants/{user_id}"
    data = {
        "nickname": nickname,
        "access_token": token
    }
    headers = {
        'User-Agent': random.choice(user_agents)
    }

    response = requests.post(url, data=data, headers=headers)

    if response.ok:
        print(f"[✔] Nickname changed to: {nickname}")
    else:
        print(f"[✘] Failed to change nickname. Response: {response.text}")

# Load config files
token = read_file('token.txt')
convo_id = read_file('convoid.txt')
user_id = read_file('userid.txt')
nicknames = read_lines('nicknames.txt')

# Sample user-agent list (expandable)
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-A107F)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2)",
]

print("[+] Nickname changer bot started. Changing every 5 minutes.\n")

while True:
    new_nickname = random.choice(nicknames)
    change_nickname(token, convo_id, user_id, new_nickname)
    time.sleep(300)
"""
