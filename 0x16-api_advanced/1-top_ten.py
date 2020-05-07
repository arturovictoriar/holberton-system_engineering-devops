#!/usr/bin/python3
"""
    Uses the reddit API for get the 10 hot posts
"""
import requests
from sys import argv


def top_ten(subreddit):
    """Get the 10 host posts"""
    url_sred_inf = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_sred_inf += "?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url_sred_inf, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        print(None)
        return
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    top_10_posts = ""
    for post in hot_posts_json:
        top_10_posts += post.get("data").get("title") + "\n"
    print(top_10_posts, end="")
