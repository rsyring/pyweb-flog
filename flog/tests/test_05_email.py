"""
    Principle #11: when it comes to external services, there can often be multiple ways to test
        around the service.  Pick the method that is most maintainable and least brittle.
    Principle #12: tests are responsible for managing expected state (usually at the start of the
        test)
    Principle #13: pytest fixtures can be very useful, but don't abuse them

    Exercises:

    1. Use mock.patch to prevent mail from actually sending
    2. Use the facilities built into flask-mail for testing
    3. Use API calls to fake-smtp-server to check the mail that gets queued
        - Use a flask fixture to clear all queued emails in fake-smtp-server to avoid cross-test
          contamination
"""
from unittest import mock

import requests

from flog.ext import mail


class Tests:

    @mock.patch('flog.cli.mail')
    def test_mock(self, m_mail, cli):
        result = cli.invoke('mail', 'pyweb@example.com')
        assert result.output == 'Test email sent to: pyweb@example.com\n'

        # TODO: demonstrate brittleness of this type of mock
        m_mail.send_message.assert_called_once_with(
            subject='Flog Test Email',
            body='Zen of Python',
            sender='from@example.com',
            recipients=['pyweb@example.com'],
        )

    def test_outbox(self, cli):
        with mail.record_messages() as outbox:
            result = cli.invoke('mail', 'pyweb@example.com')
            assert result.output == 'Test email sent to: pyweb@example.com\n'

        assert len(outbox) == 1
        msg = outbox[0]
        msg.subject == 'Flog Test Email'
        msg.body == 'Zen of Python'
        msg.sender == 'from@example.com'
        msg.recipients == ['pyweb@example.com']

    def test_fake_smtp_service(self, cli):
        requests.delete('http://localhost:1080/api/emails')

        result = cli.invoke('mail', 'pyweb@example.com')
        assert result.output == 'Test email sent to: pyweb@example.com\n'

        messages = requests.get('http://localhost:1080/api/emails', timeout=2.0).json()
        assert len(messages) == 1

        msg = messages[0]
        msg['subject'] == 'Flog Test Email'
        msg['text'] == 'Zen of Python\n'
        msg['from']['text'] == 'from@example.com'
        msg['to']['text'] == 'pyweb@example.com'
