#!/usr/bin/python3
"""Print titles of first 10 hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Query Reddit API and print first 10 hot posts."""

    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {
        "User-Agent": "python:api.advanced:v1.0 (by /u/alu_student)"
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

        posts = response.json().get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
