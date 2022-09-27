#!/usr/bin/python3
"""
reddit api that returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    if not subreddit:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(f"{url}", headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    return 0
