#Extracting a username by removing part of the URL with replace
url = input("URL: ").strip()
username = url.replace("https://twitter.com", "")
print(f"username: {username}")

#Extracting a username with a regular expression
import re

url = input("URL: ").strip()
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)

if matches:
    print(f"Username:", matches.group(1))
