#!/usr/bin/python3
"""2-recurse Module"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit."""
    if not subreddit:
        return None
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get("{}".format(url), headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)

    if req.status_code == 200:
        children = req.json().get('data').get('children')
        after = req.json().get('data').get('after')

        for i in children:
            hot_list.append(i.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list

    return None
