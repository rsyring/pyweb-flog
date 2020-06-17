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
        - write a test for hn_process_profile()
        - write stub functions
        - refactor view to use stub functions (current tests should not break)
    3. Use [patch] to mock out hn_fetch_profile()
        - it's a good idea to provide different data than live, to make sure your mock is working
    4. Use [responses] to test hn_fetch_profile()

    [webtest]: https://docs.pylonsproject.org/projects/webtest/
    [patch]: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
    [responses]: https://github.com/getsentry/responses
"""


class Tests:
    def test_form(self, web):
        resp = web.get('/hn-profile')
        assert resp.status_code == 200
        assert b'Please enter a Hacker News username:' in resp.data

    def test_hn_post(self, web):
        resp = web.post('/hn-profile', data={'username': 'rsyring'})
        assert resp.status_code == 200
        assert b'HackerNews user rsyring has 102 submissions and 404 karma.' in resp.data
