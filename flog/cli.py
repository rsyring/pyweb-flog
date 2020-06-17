import click
from flask import Blueprint

from flog.ext import mail
from flog.libs import hackernews

cli_bp = Blueprint('cli', __name__, cli_group=None)


@cli_bp.cli.command()
@click.argument('name', default='World')
def hello(name):
    print(f'Hello, {name}!')


@cli_bp.cli.command()
def error():
    raise Exception('deliberate error for testing')


@cli_bp.cli.command('mail')
@click.argument('email')
def _mail(email):
    ''' Send test email to <email> '''
    mail.send_message(
        subject='Flog Test Email',
        body='Zen of Python',
        sender='from@example.com',
        recipients=[email],
    )
    print(f'Test email sent to: {email}')


@cli_bp.cli.command()
@click.argument('username')
def hn_profile(username):
    print(hackernews.profile_stats(username, use_html=False))
