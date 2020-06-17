from flask import Blueprint, request, render_template
import requests

ident = 'hn-profile-rls'

bp = Blueprint(ident, __name__)


def hn_fetch_profile(username):
    url = f'https://hacker-news.firebaseio.com/v0/user/{username}.json'
    return requests.get(url, timeout=2.0).json()


def hn_process_profile(profile_data):
    subcount = len(profile_data['submitted'])

    return f'HackerNews user {profile_data["id"]} has {subcount} submissions and' \
        f' {profile_data["karma"]} karma.'


@bp.route(f'/{ident}', methods=('GET', 'POST'))
def hn_profile():
    if request.method == 'GET':
        return render_template('hn-profile.html')

    username = request.form['username']
    profile_data = hn_fetch_profile(username)
    return hn_process_profile(profile_data)
