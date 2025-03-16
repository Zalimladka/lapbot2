import json
import requests
from bs4 import BeautifulSoup

with open("config.json") as f:
    config = json.load(f)

FB_COOKIES = config["FB_COOKIES"]

def get_tokens():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://m.facebook.com",
        "Origin": "https://m.facebook.com"
    }
    
    response = requests.get("https://m.facebook.com", cookies=FB_COOKIES, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    fb_dtsg_input = soup.find("input", {"name": "fb_dtsg"})
    
    if fb_dtsg_input:
        fb_dtsg = fb_dtsg_input["value"]
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
