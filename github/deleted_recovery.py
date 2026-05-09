import json
import os
import requests


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

        if isinstance(data, dict):
            data = [data]

        return data

    except Exception as e:
        print("Error loading snapshots:", e)
        return []


# -----------------------------
# DETECT DELETED / CHANGED DATA (FORENSIC ENGINE)
# -----------------------------
def detect_deleted_content(username):

    snapshots = load_snapshots(username)

    if len(snapshots) < 2:
        return "not_enough_data"

    old = snapshots[-2]
    new = snapshots[-1]

    results = {}

    keys = ["bio", "location", "public_repos", "followers", "following"]

    for k in keys:

        old_val = old.get(k)
        new_val = new.get(k)

        # -----------------------------
        # REMOVED VALUE (FORENSIC SIGN)
        # -----------------------------
        if old_val is not None and new_val is None:
            results[k] = {
                "status": "REMOVED",
                "old": old_val,
                "new": None,
                "severity": "HIGH",
                "note": "Field disappeared between snapshots"
            }

        # -----------------------------
        # CHANGED VALUE
        # -----------------------------
        elif old_val != new_val:

            severity = "LOW"
            note = "Field modified"

            # numeric intelligence layer
            if isinstance(old_val, int) and isinstance(new_val, int):
                diff = new_val - old_val

                if abs(diff) > 50:
                    severity = "HIGH"
                    note = "Large anomaly detected"
                elif abs(diff) > 10:
                    severity = "MEDIUM"
                    note = "Moderate change detected"

                results[k] = {
                    "status": "CHANGED",
                    "old": old_val,
                    "new": new_val,
                    "difference": diff,
                    "severity": severity,
                    "note": note
                }

            else:
                results[k] = {
                    "status": "CHANGED",
                    "old": old_val,
                    "new": new_val,
                    "severity": severity,
                    "note": note
                }

    return results


# -----------------------------
# WAYBACK MACHINE CHECK (ARCHIVE RECOVERY)
# -----------------------------
def wayback_check(url):

    try:
        api = f"https://archive.org/wayback/available?url={url}"
        res = requests.get(api, timeout=5).json()

        snapshots = res.get("archived_snapshots", {})

        if "closest" in snapshots:
            return {
                "found": True,
                "url": snapshots["closest"]["url"],
                "note": "Archived version found"
            }

        return {
            "found": False,
            "url": None,
            "note": "No archive available"
        }

    except Exception as e:
        return {
            "found": False,
            "error": str(e),
            "note": "Wayback request failed"
        }
