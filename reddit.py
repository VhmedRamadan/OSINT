import requests
from datetime import datetime

def get_reddit_profile(username):
    url = f"https://www.reddit.com/user/{username}/about.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Error:", response.text)
            return None

        data = response.json()["data"]

        created = datetime.utcfromtimestamp(
            data["created_utc"]
        ).strftime("%Y-%m-%d %H:%M:%S")

        return {
            "platform": "Reddit",
            "username": data.get("name"),
            "karma": data.get("total_karma"),
            "icon_img": data.get("icon_img"),
            "created": created,
            "verified": data.get("verified")
        }

    except Exception as e:
        print("Exception:", e)
        return None


username = input("Enter Reddit username: ")

profile = get_reddit_profile(username)

if profile:
    print("\n=== PROFILE INFO ===")
    for key, value in profile.items():
        print(f"{key}: {value}")
else:
    print("Profile not found.")