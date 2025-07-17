import os
import json
import webbrowser
import secrets
import hashlib
from urllib.parse import urlencode
import requests
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
client_id = os.getenv("TWITTER_CLIENT_ID")
client_secret = os.getenv("TWITTER_CLIENT_SECRET")  # Not needed for PKCE, but can be stored
redirect_uri = os.getenv("TWITTER_REDIRECT_URI")
scope = os.getenv("TWITTER_SCOPE").split()
token_file = os.getenv("TWITTER_TOKEN_FILE", "token.json")

# Generate PKCE code verifier and challenge
def generate_pkce():
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = (
        hashlib.sha256(code_verifier.encode("utf-8")).digest()
    )
    code_challenge = (
        base64.urlsafe_b64encode(code_challenge)
        .decode("utf-8")
        .rstrip("=")
    )
    return code_verifier, code_challenge

def authenticate():
    code_verifier, code_challenge = generate_pkce()

    auth_params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": " ".join(scope),
        "state": secrets.token_urlsafe(16),
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }

    auth_url = f"https://twitter.com/i/oauth2/authorize?{urlencode(auth_params)}"

    print("🔗 Open the following URL in your browser and log in:")
    print(auth_url)
    webbrowser.open(auth_url)

    redirect_response = input("\n📥 Paste the full redirect URL after authorization:\n")

    # Extract the code from the redirect URL
    from urllib.parse import urlparse, parse_qs
    parsed_url = urlparse(redirect_response)
    query_params = parse_qs(parsed_url.query)
    auth_code = query_params.get("code", [None])[0]

    if not auth_code:
        print("❌ Authorization code not found.")
        return

    # Exchange auth code for token
    token_url = "https://api.twitter.com/2/oauth2/token"
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "code_verifier": code_verifier,
    }

    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        print(f"❌ Token exchange failed: {response.status_code}\n{response.text}")
        return

    token = response.json()
    with open(token_file, "w") as f:
        json.dump(token, f)

    print("✅ Access token saved to", token_file)

if __name__ == "__main__":
    import base64
    authenticate()
