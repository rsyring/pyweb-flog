"""
    Principle #1: Just get started (with something trivial)

    Sometimes I get hung up with all the possible variations involved in building
    something, especially at the very beginning of a project.  When I feel "stuck' this way,
    similar IMO to writer's block, I find the best remedy is to just get some tests written down.
    I can then iterate from there and let the architecture reveal itself based on actual needs,
    avoiding YAGNI.
"""


class Tests:

    def test_cli_hello(self, cli):
        result = cli.invoke('hello')
        assert result.output == 'Hello, World!\n'

        result = cli.invoke('hello', 'pyweb')
        assert result.output == 'Hello, pyweb!\n'

    def test_web_hello(self, web):
        resp = web.get('/hello')
        assert resp.data == b'Hello, World!'

        resp = web.get('/hello/pyweb')
        assert resp.data == b'Hello, pyweb!'

    def test_email_send(self, cli):
        result = cli.invoke('mail', 'pyweb@example.com')
        assert result.output == 'Test email sent to: pyweb@example.com\n'
