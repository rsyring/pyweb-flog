from flask import Blueprint, request, render_template
import requests

ident = 'hn-profile-1'

bp = Blueprint(ident, __name__)


@bp.route(f'/{ident}', methods=('GET', 'POST'))
def hn_profile():
    if request.method == 'GET':
        return render_template('hn-profile.html')

    username = request.form['username']
    url = f'https://hacker-news.firebaseio.com/v0/user/{username}.json'
    profile = requests.get(url, timeout=2.0).json()
    subcount = len(profile['submitted'])

    return f'HackerNews user {username} has {subcount} submissions and' \
        f' {profile["karma"]} karma.'
