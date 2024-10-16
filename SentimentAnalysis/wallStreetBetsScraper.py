# Reddit API is used to scrape the hot posts from the wallstreetbets subreddit.
# Intded for Sentiment Analysis of Wallstreetbets Reddit Posts
CLIENT_ID = "G18X3v_teLmzHF5ImA2z_w"
SECRET_KEY = "aG0mz4dcFOr8-2hVW_Gj1NbCQ7zAig"

import requests
import json

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# For external file containing password
# with open('pw.text', 'r') as f:
#     pw = f.read()

login = {
    'grant_type': 'password',
    'username': 'Mopann',
    'password': 'H8terslive'
}

headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', 
                    auth=auth, 
                    data=login, 
                    headers=headers)

ACCESS_TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f'bearer {ACCESS_TOKEN}'}}

permissions = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()

#Get hot posts from wallstreetbets
hot_posts = requests.get('https://oauth.reddit.com/r/wallstreetbets/hot', headers=headers).json()

with open('hot_posts.json', 'w') as f:
    json.dump(hot_posts, f)

# Get Title of posts
for post in hot_posts['data']['children']:
    print(post['data']['title'])