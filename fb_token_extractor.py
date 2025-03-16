import requests
import json

def get_tokens():
    # Replace with your FB cookies
    cookies = {
        "c_user": "YOUR_C_USER",
        "xs": "YOUR_XS_TOKEN"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get("https://m.facebook.com", cookies=cookies, headers=headers)
    
    # Extract fb_dtsg token
    fb_dtsg = response.text.split('{"token":"')[1].split('"')[0]

    tokens = {
        "c_user": cookies["c_user"],
        "xs": cookies["xs"],
        "fb_dtsg": fb_dtsg
    }

    with open("tokens.json", "w") as f:
        json.dump(tokens, f)

    print("✅ Tokens Saved Successfully!")

get_tokens()
