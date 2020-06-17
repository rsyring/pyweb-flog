import click

from flask import Flask
from flask.cli import FlaskGroup

import flog.cli
from flog.ext import init_ext
from flog.libs.testing import CLIRunner
from flog.views import all_blueprints


def create_app(testing=False):
    app = Flask(__name__)
    app.test_cli_runner_class = CLIRunner
    app.testing = testing

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:password@localhost:54321/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext(app)

    for bp in all_blueprints:
        app.register_blueprint(bp)
    app.register_blueprint(flog.cli.cli_bp)

    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the Wiki application."""
