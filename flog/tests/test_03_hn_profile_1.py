class Tests:
    def test_form(self, web):
        resp = web.get('/hn-profile-1')
        assert resp.status_code == 200
        assert b'Please enter a Hacker News username:' in resp.data

    def test_hn_post(self, web):
        resp = web.post('/hn-profile-1', data={'username': 'rsyring'})
        assert resp.status_code == 200
        assert b'HackerNews user rsyring has 102 submissions and 404 karma.' in resp.data
