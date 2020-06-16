
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

