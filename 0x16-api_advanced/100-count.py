#!/usr/bin/python3
"""
    Uses the reddit API for parseing the title of all hot articles,
    and prints a sorted count of given keywords
"""
import requests
from sys import argv


def recurse(subreddit, word_list, counted_word, after=""):
    """Get the all host posts"""
    if after is None:
        return counted_word
    url_sred_inf = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_sred_inf += "?limit=100&after={}".format(after)
    headers = {'user-agent': 'req'}
    response = requests.get(url_sred_inf, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return None
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    for post in hot_posts_json:
        title = (post.get("data").get("title"))
        for word in word_list:
            counted_word[word] += title.lower().split().count(word.lower())
    after = r_json.get("data").get("after")
    return recurse(subreddit, word_list, counted_word, after)


def count_words(subreddit, word_list):
    counted_word = {}
    for word in word_list:
        counted_word[word] = 0
    w_count = recurse(subreddit, word_list, counted_word)
    if not w_count:
        return
    sort_words = sorted(w_count.items(), key=lambda t: t[::-1])
    sort_des_words = sorted(sort_words, key=lambda tup: tup[1], reverse=True)
    print_counted_words = ""
    for word, count in sort_des_words:
        if count:
            print_counted_words += "{}: {}\n".format(word, count)
    print(print_counted_words, end="")
