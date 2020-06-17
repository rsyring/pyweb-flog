from flask import Blueprint, request, render_template

from ..libs import hackernews

ident = 'hn-profile-rls'

bp = Blueprint(ident, __name__)


@bp.route(f'/{ident}', methods=('GET', 'POST'))
def hn_profile():
    if request.method == 'GET':
        return render_template('hn-profile.html')

    username = request.form['username']
    profile_data = hackernews.fetch_profile(username)
    subcount, karma = hackernews.process_profile(profile_data)
    return f'HackerNews user {username} has {subcount} submissions and' \
        f' {karma} karma.'
