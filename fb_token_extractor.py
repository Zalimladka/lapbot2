import json
import requests

with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]

def get_tokens():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.facebook.com",
        "Origin": "https://www.facebook.com"
    }

    response = requests.get("https://www.facebook.com/api/graphql/", cookies=FB_COOKIES, headers=headers)
    
    if "fb_dtsg" in response.text:
        fb_dtsg = response.text.split('DTSGInitialData",[],{"token":"')[1].split('"')[0]
    else:
        print("❌ FB_DTSG Not Found")
        fb_dtsg = None

    tokens = {
        "fb_dtsg": fb_dtsg,
        "c_user": FB_COOKIES["c_user"],
        "xs": FB_COOKIES["xs"]
    }

    with open("tokens.json", "w") as f:
        json.dump(tokens, f, indent=4)

    print("✅ Tokens Extracted Successfully!")

if __name__ == "__main__":
    get_tokens()

