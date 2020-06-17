import click
from flask import Blueprint

from flog.ext import mail

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
    mail.send_mail(
        'Flog Test Email',
        'Zen of Python',
        'from@example.com',
        [email],
        fail_silently=False,
    )
    print(f'Test email sent to: {email}')
