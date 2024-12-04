import requests
import os
import sys
import re

year = 2024

def fetch_input(day, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)
    if response.ok:
        return response.text
    else:
        print("Error fetching input data")
        return None

def save_input(day, session_cookie):
    data = fetch_input(day, session_cookie)
    if not data:
        return
    with open(f"solutions/{day}.in", "w") as f:
        f.write(data)
    print(f"Input data for {year}/{day} saved to solutions/{day}.in")

def main():
    if sys.argv[1] == "clear":
        clear_inputs()
        return
    match = re.match(r"(\d{1,2})", sys.argv[1])
    if not match:
        print("Invalid argument. Please provide a day in the format DD or use 'clear' to delete all input files.")
        return
    day = match.group(1)
    if int(day) > 25 or int(day) < 1:
        print("Invalid day. Please provide a day between 1 and 25.")
        return
    session_cookie = open("SESSION_COOKIE.txt").read().strip()
    save_input(day, session_cookie)

def clear_inputs():
    for file in os.listdir("solutions"):
        if file.endswith(".in"):
            print(f"Deleting {file}")
            os.remove(f"solutions/{file}")

main()
