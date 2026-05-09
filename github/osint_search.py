import requests
import subprocess


# -----------------------------
# GITHUB CHECK (REAL OSINT)
# -----------------------------
def check_github(username):

    try:
        url = f"https://api.github.com/users/{username}"
        headers = {
            "User-Agent": "OSINT-Tool"
        }

        r = requests.get(url, headers=headers, timeout=5)

        return {
            "exists": r.status_code == 200,
            "status_code": r.status_code
        }

    except Exception as e:
        return {
            "exists": False,
            "error": str(e)
        }


# -----------------------------
# SHERLOCK INTEGRATION (REAL OSINT ENUMERATION)
# -----------------------------
def sherlock_search(username):

    try:
        result = subprocess.run(
            ["sherlock", username, "--print-found"],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return {
                "found": False,
                "data": "No matches found"
            }

        return {
            "found": True,
            "data": output
        }

    except Exception as e:
        return {
            "found": False,
            "error": str(e)
        }


# -----------------------------
# CROSS PLATFORM OSINT SEARCH (IMPROVED)
# -----------------------------
def cross_platform_search(username):

    results = {}

    # -----------------------------
    # GitHub verification
    # -----------------------------
    github_result = check_github(username)

    results["GitHub"] = {
        "exists": github_result.get("exists"),
        "status_code": github_result.get("status_code"),
        "confidence": "HIGH" if github_result.get("exists") else "LOW"
    }

    # -----------------------------
    # OSINT ENUMERATION (SIMULATED + STRUCTURED)
    # -----------------------------
    platforms = [
        "Twitter/X",
        "Instagram",
        "Reddit",
        "TikTok",
        "Facebook"
    ]

    for p in platforms:

        results[p] = {
            "url": f"https://{p.lower().replace('x', 'twitter').replace('/', '')}.com/{username}",
            "status": "UNKNOWN",
            "confidence": "LOW (unverified)"
        }

    # -----------------------------
    # Sherlock real OSINT
    # -----------------------------
    sherlock_result = sherlock_search(username)

    results["Sherlock"] = sherlock_result

    return results
