import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MY_GITHUB_USERNAME = os.getenv("MY_GITHUB_USERNAME")
MY_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
LINKEDIN_PERSON_URN = os.getenv("LINKEDIN_PERSON_URN")

# Twitter App Settings
TWITTER_CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
TWITTER_CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
TWITTER_REDIRECT_URI = os.getenv("TWITTER_REDIRECT_URI")
TWITTER_SCOPE = os.getenv("TWITTER_SCOPE", "tweet.read tweet.write users.read offline.access")
TWITTER_TOKEN_FILE = os.getenv("TWITTER_TOKEN_FILE", "token.json")


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
