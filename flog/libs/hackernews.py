import requests


def fetch_profile(username):
    url = f'https://hacker-news.firebaseio.com/v0/user/{username}.json'
    return requests.get(url, timeout=2.0).json()


def process_profile(profile_data):
    subcount = len(profile_data['submitted'])

    return f'HackerNews user {profile_data["id"]} has {subcount} submissions and' \
        f' {profile_data["karma"]} karma.'
