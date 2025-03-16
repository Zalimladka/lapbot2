import requests
import json

with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]
FB_DTSG = config["FB_DTSG"]
GROUPS = config["groups_info"]

def change_nickname(group_id, user_id, nickname):
    url = "https://www.facebook.com/api/graphql/"

    payload = {
        "av": FB_COOKIES["c_user"],
        "fb_dtsg": FB_DTSG,
        "variables": json.dumps({
            "input": {
                "client_mutation_id": "1",
                "actor_id": FB_COOKIES["c_user"],
                "group_id": group_id,
                "member_id": user_id,
                "nickname": nickname,
                "source": "GROUPS_COMET_MEMBER_DETAILS"
            }
        }),
        "doc_id": "3828654037231031"
    }

    headers = {
        "authority": "www.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    response = requests.post(url, data=payload, cookies=FB_COOKIES, headers=headers)

    if "error" not in response.text:
        print(f"✅ Nickname Changed for {user_id}")
    else:
        print(f"❌ Nickname Change Failed for {user_id}")

if __name__ == "__main__":
    for group_id, group_data in GROUPS.items():
        for user_id in group_data["users"]:
            change_nickname(group_id, user_id, "🔥 King 🔥")
