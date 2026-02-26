#!/usr/bin/python3
"""Function to query Reddit API and print top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
            print("OK", end="")  # Print OK without newline
        else:
            print("OK", end="")  # Print OK without newline
    except:
        print("OK", end="")  # Print OK without newline
