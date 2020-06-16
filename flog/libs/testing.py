from flask.testing import FlaskCliRunner


class CLIRunner(FlaskCliRunner):
    def invoke(self, *args, **kwargs):
        # Letting Click catch the exception makes it too easy to miss an exception accidently.
        kwargs.setdefault('catch_exceptions', False)
        return super().invoke(None, args, **kwargs)
