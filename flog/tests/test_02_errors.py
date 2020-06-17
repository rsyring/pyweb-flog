import pytest

import flog.app


class Tests:

    def test_cli_error(self, cli):
        with pytest.raises(Exception) as excinfo:
            # TODO: Show what this looks like when not caught
            cli.invoke('error')
        assert 'deliberate' in str(excinfo.value)

    def test_cli_error_2(self, cli):
        result = cli.invoke('error', catch_exceptions=True)
        assert result.exception

    def test_web_error(self, web):
        with pytest.raises(Exception) as excinfo:
            # TODO: Show what this looks like when not caught
            web.get('/error')
        assert 'deliberate' in str(excinfo.value)

    def test_web_error2(self):
        app = flog.app.create_app()
        web = app.test_client()

        resp = web.get('/error')
        assert resp.status_code == 500
