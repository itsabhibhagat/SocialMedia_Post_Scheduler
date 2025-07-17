import requests
import webbrowser
import urllib.parse
import pkce

# 🔁 Replace these with your app credentials
CLIENT_ID = "YTI4elNKZUQzQUhLZXkzWnowb1g6MTpjaQ"
REDIRECT_URI = "http://localhost:3000/twitter/callback"
SCOPES = "tweet.read tweet.write users.read offline.access"

# 1. Generate PKCE challenge
code_verifier, code_challenge = pkce.generate_pkce_pair()

# 2. Build authorization URL
params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPES,
    "state": "secure_random_state",
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
}
auth_url = f"https://twitter.com/i/oauth2/authorize?{urllib.parse.urlencode(params)}"

print("\n🔑 Open this URL in browser and login:\n")
print(auth_url)
webbrowser.open(auth_url)

# 3. After login, get code from URL
code = input("\nPaste the code parameter from the redirect URL here: ")

# 4. Exchange code for token
token_url = "https://api.twitter.com/2/oauth2/token"
data = {
    "code": code,
    "grant_type": "authorization_code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "code_verifier": code_verifier,
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

response = requests.post(token_url, data=data, headers=headers)
print("\n🎉 Tokens:")
print(response.json())
