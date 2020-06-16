import click

from flask import Flask
from flask.cli import FlaskGroup

import flog.cli
from flog.ext import db
from flog.libs.testing import CLIRunner
from flog.views import all_blueprints



def create_app():
    app = Flask(__name__)
    app.test_cli_runner_class = CLIRunner

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:password@localhost:54321/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    for bp in all_blueprints:
        app.register_blueprint(bp)
    app.register_blueprint(flog.cli.cli_bp)

    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the Wiki application."""
