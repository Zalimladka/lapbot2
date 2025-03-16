import requests
import json

# Tokens.json se tokens uthao
with open("tokens.json") as f:
    tokens = json.load(f)

# Config.json se groups info uthao
with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = {
    "c_user": tokens["c_user"],
    "xs": tokens["xs"]
}

FB_DTSG = tokens["fb_dtsg"]
GROUPS = config["groups_info"]

def change_nickname(group_id, user_id, nickname):
    url = "https://www.facebook.com/api/graphql/"

    payload = {
        "av": FB_COOKIES["c_user"],
        "fb_dtsg": FB_DTSG,
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
        print(f"❌ Failed for {user_id}")

if __name__ == "__main__":
    for group_id, group_data in GROUPS.items():
        if "all" in group_data["users"]:
            members_url = f"https://m.facebook.com/groups/{group_id}/members/"
            response = requests.get(members_url, cookies=FB_COOKIES)
            user_ids = set([x.split(';')[0] for x in response.text.split('member_id=') if x.startswith('1')])

            for user_id in user_ids:
                change_nickname(group_id, user_id, "🔥 King 🔥")
        else:
            for user_id in group_data["users"]:
                change_nickname(group_id, user_id, "🔥 King 🔥")

