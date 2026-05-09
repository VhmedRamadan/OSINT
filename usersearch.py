import requests

platforms = {
    "GitHub": "https://api.github.com/users/{}",
    "Twitter": "https://api.twitter.com/2/users/by/username/{}",
    "Reddit": "https://www.reddit.com/user/{}/about.json"
}

username = input("Enter username: ")

for platform, url in platforms.items():
    try:
        response = requests.get(url.format(username), timeout=5)

        if response.status_code == 200:
            print(f"[+] {username} exists on {platform}")
        elif response.status_code == 404:
            print(f"[-] {username} not found on {platform}")
        elif response.status_code == 401:
            print(f"[x] {platform} does not authorize looking for user data")
        elif response.status_code == 429:
            print(f"[x] {platform} recieved too many requests, slow down")    
        else:
            print(f"[?] {platform}: status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[!] Error checking {platform}")
