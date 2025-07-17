import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

TOKEN_FILE = os.getenv("TWITTER_TOKEN_FILE", "token.json")
CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")  # Optional for refresh
TOKEN_URL = "https://api.twitter.com/2/oauth2/token"

def load_token():
    with open(TOKEN_FILE, "r") as f:
        return json.load(f)

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        json.dump(token, f)

def refresh_access_token(refresh_token):
    print("🔁 Refreshing Twitter access token...")
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code != 200:
        raise Exception(f"Failed to refresh token: {response.status_code}\n{response.text}")

    new_token = response.json()

    # Preserve original refresh_token if not returned in response
    if "refresh_token" not in new_token:
        new_token["refresh_token"] = refresh_token

    save_token(new_token)
    return new_token["access_token"]


def get_valid_access_token():
    token = load_token()

    if "refresh_token" in token:
        return refresh_access_token(token["refresh_token"])
    else:
        raise Exception("No refresh token found in token.json.")

def post_to_twitter(message):
    access_token = get_valid_access_token()

    if len(message) > 280:
        message = message[:277] + "..."

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = { "text": message }
    url = "https://api.twitter.com/2/tweets"

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ Tweet posted successfully.")
    else:
        print(f"❌ Twitter error: {response.status_code}\n{response.text}")
        raise Exception("Twitter post failed.")

# if __name__ == "__main__":
#     test_message = "🚀 Hello world! Testing Twitter bot with auto-refresh. #BuildInPublic"
#     post_to_twitter(test_message)
