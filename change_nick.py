import requests
import json

with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
GROUPS = config["groups_info"]

def change_nickname(group_id, user_id, nickname):
    url = "https://www.facebook.com/api/graphql/"

    payload = {
        "variables": {
            "input": {
                "client_mutation_id": "1",
                "actor_id": FB_COOKIES["c_user"],
                "group_id": group_id,
                "member_id": user_id,
                "nickname": nickname
            }
        }
    }

    response = requests.post(url, json=payload, cookies=FB_COOKIES)

    if response.status_code == 200:
        print(f"✅ Nickname Changed for {user_id}")
    else:
        print(f"❌ Nickname Change Failed for {user_id}")

if __name__ == "__main__":
    for group_id, group_data in GROUPS.items():
        for user_id in group_data["users"]:
            change_nickname(group_id, user_id, "🔥 King 🔥")
