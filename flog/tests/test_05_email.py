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


class Tests:

    def test_email_send(self, cli):
        result = cli.invoke('mail', 'pyweb@example.com')
        assert result.output == 'Test email sent to: pyweb@example.com\n'

