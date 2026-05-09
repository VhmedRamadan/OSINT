import requests
import json
import os
from datetime import datetime


# -----------------------------
# TOKEN (IMPORTANT)
# -----------------------------
token = "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"


# -----------------------------
# GET FOLLOWERS (FIXED)
# -----------------------------
def get_github_user(username):

    if not username:
        return None

    url = f"https://api.github.com/users/{username}"

    headers = {
        "User-Agent": "OSINT-Forensics-Tool",
        "Accept": "application/vnd.github+json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        r = requests.get(url, headers=headers)

        if r.status_code == 403:
            return {"error": "rate_limit_or_invalid_token"}

        if r.status_code == 404:
            return {"error": "user_not_found"}

        if r.status_code != 200:
            return {"error": f"unknown_error_{r.status_code}"}

        data = r.json()

        return {
            "username": data.get("login"),
            "name": data.get("name"),
            "bio": data.get("bio"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "public_repos": data.get("public_repos"),
            "location": data.get("location"),
            "profile_url": data.get("html_url"),

            # 🔥 forensic additions
            "created_at": data.get("created_at"),
            "updated_at": data.get("updated_at"),
            "timestamp": str(datetime.now())
        }

    except Exception as e:
        return {"error": str(e)}

def get_followers(username, limit=5):

    url = f"https://api.github.com/users/{username}/followers?per_page={limit}"

    headers = {
        "User-Agent": "OSINT-Forensics-Tool",
        "Accept": "application/vnd.github+json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            return []

        data = r.json()

        return [u["login"] for u in data]

    except Exception as e:
        print("error:", e)
        return []



# -----------------------------
# SAVE SNAPSHOT (FIXED)
# -----------------------------
def save_snapshot(username, data):

    if not data:
        return

    os.makedirs("data", exist_ok=True)

    filename = f"data/{username}.json"

    # load old
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                old_data = json.load(f)
            except:
                old_data = []
    else:
        old_data = []

    if isinstance(old_data, dict):
        old_data = [old_data]

    # -----------------------------
    # prevent duplicate snapshot
    # -----------------------------
    if old_data and old_data[-1].get("timestamp") == data.get("timestamp"):
        return

    old_data.append(data)

    # -----------------------------
    # save
    # -----------------------------
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(old_data, f, indent=4, ensure_ascii=False)
