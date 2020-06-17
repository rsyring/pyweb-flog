import importlib
import pathlib

from flask import Blueprint

bp = Blueprint('default', __name__)

all_blueprints = [bp]


def dynamic_view_loading():
    """
        Import any .py files in flog/views and include the bp attribute of that module in
        `all_blueprints`.
    """
    pymod_paths = [fpath for fpath in pathlib.Path(__file__).parent.glob('*.py')
                if fpath.name != '__init__.py']

    for pymod_fpath in pymod_paths:
        pymod = importlib.import_module(f'flog.views.{pymod_fpath.stem}')
        all_blueprints.append(pymod.bp)


dynamic_view_loading()


@bp.route('/hello')
@bp.route('/hello/<name>')
def hello(name='World'):
    return f'Hello, {name}!'


@bp.route('/error')
def error():
    raise Exception('deliberate error for testing purposes')
