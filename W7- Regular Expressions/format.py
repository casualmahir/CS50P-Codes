#Reformatting "last, first" with split (no regex)
name = input("What's your name? ")
if ", " in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")

#Reformatting "last, first" with re.search and groups
import re

name = input("What's your name?").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")
