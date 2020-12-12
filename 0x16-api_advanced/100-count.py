#!/usr/bin/python3
"""
    Query the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
"""

import requests


def convert_lower(w, i, len_w):
    """Convert strings to lowercase"""
    if i >= len_w:
        return None

    w[i] = w[i].lower()
    convert_lower(w, i + 1, len_w)

    return None


def count_word_title(title, i, len_t, dict_words_unique):
    """Store repeating string in hash table"""
    if i >= len_t:
        return None

    if title[i] in dict_words_unique:
        dict_words_unique[title[i]] += 1

    count_word_title(title, i + 1, len_t, dict_words_unique)

    return None


def store_title_word_hash(list_title, i, len_l, dict_words_unique):
    """Run trough a list of hot titles"""
    if i >= len_l:
        return None

    title = list_title[i]["data"]["title"].lower().split(" ")

    count_word_title(title, 0, len(title), dict_words_unique)

    store_title_word_hash(list_title, i + 1, len_l, dict_words_unique)

    return None


def store_given_word_hash(w, i, len_w, dict_words, type_d):
    """store given words in hash tables"""
    if i >= len_w:
        return None
    if type_d == "r":
        if w[i] in dict_words:
            dict_words[w[i]] += 1
        else:
            dict_words[w[i]] = 1
    elif type_d == "u":
        dict_words[w[i]] = 0

    store_given_word_hash(w, i + 1, len_w, dict_words, type_d)

    return None


def print_words(w, i, len_wn, dict_words_repeated):
    """Print the repeated strings"""
    if i >= len_wn:
        return None

    if w[i][1] > 0:
        print("{}: {}".format(w[i][0], dict_words_repeated[w[i][0]] * w[i][1]))

    print_words(w, i + 1, len_wn, dict_words_repeated)

    return None


def get_all_hot_articles(subreddit, word_list, dict_words_unique, after=""):
    """Get the all articles"""
    if after is None:
        return dict_words_unique
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url += "?limit=100&after={}".format(after)
    headers_m = {'User-agent': 'botsito'}
    redirect = False

    r = requests.get(url, allow_redirects=redirect, headers=headers_m)
    if r.status_code != 200:
        return None

    articles = r.json().get("data").get("children")

    store_title_word_hash(articles, 0, len(articles), dict_words_unique)

    after = r.json().get("data").get("after")
    return get_all_hot_articles(subreddit, word_list, dict_words_unique, after)


def count_words(subreddit, word_list):
    """Count the number of time a word in word_list is name
    in the hot articles subrredt"""
    convert_lower(word_list, 0, len(word_list))

    words_repeated = {}
    store_given_word_hash(word_list, 0, len(word_list), words_repeated, "r")

    words_unique = {}
    store_given_word_hash(word_list, 0, len(word_list), words_unique, "u")

    words_filled = get_all_hot_articles(subreddit, word_list, words_unique)
    if not words_filled:
        return

    sort_words = sorted(words_filled.items(), key=lambda t: t[::-1])
    sort_des_words = sorted(sort_words, key=lambda tup: tup[1], reverse=True)

    print_words(sort_des_words, 0, len(sort_des_words), words_repeated)
