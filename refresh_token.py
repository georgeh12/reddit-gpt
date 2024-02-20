import praw
import json
import random
import string

# Copy template below into login.json
"""
credentials ={
    "username":"",
    "password": "",
    "client_id":"",
    "client_secret":"",
    "user_agent":"script by u/user",
    "redirect_uri":"http://localhost:8080/"
}
"""
# Load the JSON file with your credentials
with open('login.json') as f:
    credentials = json.load(f)

reddit = praw.Reddit(
    username=credentials['username'],
    password=credentials['password'],
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    user_agent=credentials['user_agent'],
    redirect_uri=credentials['redirect_uri']
)
state = ''.join(random.choice(string.digits) for _ in range(14))
print(reddit.user.me())
print(reddit.auth._reddit._core._authorizer.access_token)
# Open the following link to authorize this app. The resulting link has the refresh token in the url.
print(reddit.auth.url(scopes=["*"], state=state, duration="permanent"))
# Copy the resulting url from the app authorization as the refresh_token: [state]-[code]