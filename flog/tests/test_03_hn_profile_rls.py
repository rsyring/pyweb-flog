"""
    Principle #3: make tests as close to the "real world" as possible
    Principle #4: it's helpful to refactor code to make it easier to test
    Principle #5: use mocking as needed to avoid depending on the "real world" for data

    The tests below are effective, but brittle.  If the source data changes (e.g. I submit another
    comment on HN or my karma goes up) or there is a network blip, the second test will fail.

    Additionally, the first test passes but misses a bug.  Run the flask web server and submit
    a user name and you will find a bug.

    Exercises (create a new test file and a new view file):

    1. Use the [Webtest] library to do better form handling tests that expose the bug in our view
         - You will probably want to use a pytest fixture to load the webtest client when needed
           (see conftest.py)
         - Fix the bug
    2. Refactor the view to use a two step process to get and then process the user profile data
        - write a test for hn_process_user_data()
        - write stub functions
        - refactor view to use stub functions (current tests should not break)
    3. Use [patch] to mock out hn_fetch_user()
        - it's a good idea to provide different data than live, to make sure your mock is working
    4. Use [responses] to test hn_fetch_user()

    [webtest]: https://docs.pylonsproject.org/projects/webtest/
    [patch]: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
    [responses]: https://github.com/getsentry/responses
"""
from unittest import mock

import pytest
import responses
import webtest

from flog.libs import hackernews
from flog.views import hn_profile_rls


@pytest.fixture()
def wt(app):
    return webtest.TestApp(app)


class Tests:
    example_profile = {
        'karma': '123',
        'submitted': [4, 5, 6]
    }

    def test_hn_process_profile(self):
        result = hackernews.process_profile(self.example_profile)
        assert result == (3, '123')

    @responses.activate
    def test_hn_fetch_profile(self):
        responses.add(
            responses.GET,
            'https://hacker-news.firebaseio.com/v0/user/rsyring.json',
            json={'foo': 'bar'}
        )
        # TODO: demonstrate what happens if 'rsyring' is changed
        result = hackernews.fetch_profile('rsyring')
        # TODO: note that we are only testing that the data is passed through.  It doesn't have to
        # be actual profile data.
        assert result == {'foo': 'bar'}

    def test_view(self, wt):
        resp = wt.get('/hn-profile-rls')
        resp.form['username'] = 'rsyring'

        with mock.patch.object(hn_profile_rls.hackernews, 'fetch_profile') as m_fetch_profile:
            m_fetch_profile.return_value = self.example_profile

            resp2 = resp.form.submit()
            assert 'HackerNews user rsyring has 3 submissions and 123 karma.' in resp2

            m_fetch_profile.assert_called_once_with('rsyring')

    def test_view_invalid_username(self, wt):
        resp = wt.get('/hn-profile-rls')
        resp.form['username'] = 'rsyrin'

        with hackernews.mock_profile():
            resp2 = resp.form.submit()
            assert 'No HackerNews user: <strong>rsyrin</strong>' in resp2
