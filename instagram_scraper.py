from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Target profile
USERNAME = "instagram"   # change this

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


def login_instagram(driver, IG_USER, IG_PASS):
    try:
        time.sleep(2)
        # Wait for username field (means login page is shown)
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "pass")

        print("[+] Login page detected. Logging in...")

        username_input.clear()
        username_input.send_keys(IG_USER)

        password_input.clear()
        password_input.send_keys(IG_PASS)
        password_input.send_keys(Keys.RETURN)

        print("[+] Logged in successfully")

    except Exception as e:
        print("[+] Login not required or failed:", e)
driver.get("https://www.instagram.com/")
login_instagram(driver, "bonusporfavor", "please_give_me_bonus")
time.sleep(5)
# Open Instagram profile
driver.get(f"https://www.instagram.com/{USERNAME}/")

# Wait for page to load
time.sleep(10)
try:
    # Username (top of page)
    username = driver.find_element(By.XPATH, "//h2").text

    # Stats: posts, followers, following
    stats = driver.find_elements(By.XPATH, "//ul/li")

    posts = stats[0].text
    followers = stats[1].text
    following = stats[2].text

    print("Username:", username)
    print("Posts:", posts)
    print("Followers:", followers)
    print("Following:", following)
    posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

    links = []
    for post in posts:
        link = post.get_attribute('href')
        if link not in links:
            links.append(link)

    print("Collected links:", links)
#     for link in links[:5]:  # limit to 5 for safety
#         driver.get(link)
#         time.sleep(3)

#         try:
            # caption = driver.find_element(By.CLASS_NAME, "_a9zr')]").text
#             print("Caption:", caption)
#         except:
#             print("No caption found")

#     print("-" * 50)
except Exception as e:
    print("Error:", e)

# Close browser
driver.quit()