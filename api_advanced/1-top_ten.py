#!/usr/bin/python3
"""Function to query Reddit API and print top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit is valid (status code 200)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            # Print title for each post
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # Invalid subreddit
            print(None)
    except:
        print(None)
