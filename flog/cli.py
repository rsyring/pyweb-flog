import click
from flask import Blueprint


cli_bp = Blueprint('cli', __name__, cli_group=None)


@cli_bp.cli.command()
@click.argument('name', default='World')
def hello(name):
    print(f'Hello, {name}!')


@cli_bp.cli.command()
def error():
    raise Exception('deliberate error for testing')
