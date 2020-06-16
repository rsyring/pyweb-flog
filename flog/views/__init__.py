from flask import Blueprint

from . import hn_profile_1

bp = Blueprint('default', __name__)

all_blueprints = (
    bp,
    hn_profile_1.bp,
)


@bp.route('/hello')
@bp.route('/hello/<name>')
def hello(name='World'):
    return f'Hello, {name}!'


@bp.route('/error')
def error():
    raise Exception('deliberate error for testing purposes')
