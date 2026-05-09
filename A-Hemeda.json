import json
import os
from datetime import datetime


# -----------------------------
# LOAD SNAPSHOTS
# -----------------------------
def load_snapshots(username):
    filename = f"data/{username}.json"

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # ensure list format
        if isinstance(data, dict):
            data = [data]

        return data

    except Exception as e:
        print("Error loading snapshots:", e)
        return []


# -----------------------------
# COMPARE SNAPSHOTS
# -----------------------------
def compare_snapshots(old, new):
    changes = {}

    keys = ["followers", "following", "public_repos", "bio", "location"]

    for k in keys:
        old_val = old.get(k)
        new_val = new.get(k)

        if old_val != new_val:
            change_entry = {
                "old": old_val,
                "new": new_val
            }

            # -----------------------------
            # NUMERIC CHANGE ANALYSIS
            # -----------------------------
            if isinstance(old_val, int) and isinstance(new_val, int):
                diff = new_val - old_val
                change_entry["difference"] = diff

                # suspicious detection
                if k == "followers" and diff > 50:
                    change_entry["alert"] = "⚠️ Sudden increase in followers"

                if k == "following" and diff > 50:
                    change_entry["alert"] = "⚠️ Sudden increase in following"

            # -----------------------------
            # TEXT CHANGE DETECTION
            # -----------------------------
            if isinstance(old_val, str) and isinstance(new_val, str):
                if old_val != new_val:
                    change_entry["note"] = "Text changed"

            changes[k] = change_entry

    # -----------------------------
    # ADD TIMESTAMP INFO
    # -----------------------------
    changes["analysis_time"] = str(datetime.now())

    return changes


# -----------------------------
# UI FUNCTION (FOR STREAMLIT)
# -----------------------------
def analyze_changes_ui(username):
    snapshots = load_snapshots(username)

    if len(snapshots) == 0:
        return {
            "status": "no_data",
            "message": "No snapshots found for this user."
        }

    if len(snapshots) == 1:
        return {
            "status": "only_one",
            "message": "Only one snapshot available. Cannot compare."
        }

    old = snapshots[-2]
    new = snapshots[-1]

    result = compare_snapshots(old, new)

    return {
        "status": "success",
        "data": result,
        "old_timestamp": old.get("timestamp"),
        "new_timestamp": new.get("timestamp")
    }
