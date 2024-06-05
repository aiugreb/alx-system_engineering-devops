#!/usr/bin/python3
""" api for subreddit info"""
import requests


def number_of_subscribers(subreddit):
    """ reddit api"""
    resp = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/125.0.0.0 Safari/537.36"
        },
        allow_redirects=False
    )
    if resp.status_code == 200:
        results = resp.json().get("data")
        return results.get("subscribers")
    else:
        return 0
