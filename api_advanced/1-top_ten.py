#!/usr/bin/python3
"""Query Reddit API and print the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts of a subreddit."""

    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {
        "User-Agent": "python:api.advanced:v1.0 (by /u/student)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data").get("title"))

    except Exception:
        print(None)
