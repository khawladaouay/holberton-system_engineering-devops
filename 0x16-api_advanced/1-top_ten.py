#!/usr/bin/python3
"""1-top_ten Module"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit."""
    if not subreddit:
        print('None')
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(f"{url}", headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    if req.status_code == 200:
        for i in req.json().get('data').get('children'):
            if i.get('data').get('title'):
                print(i.get('data').get('title'))
    else:
        print('None')