"""
    Principle #6: it's often useful to create CLI commands that make it easy to run library code
    Principle #7: most of the time, your library code & data structures should be "context agnostic"
    Principle #8: but, sometimes it makes more sense to share library code and make it adaptable to
      the context.
    Principle #9: it's really easy to only test happy paths, don't do that.  Test the unhappy paths
      too.

    Exercises:

    1. Refactor the view code from the last exercise and put it in flog/libs/hackernews.py
    2. Make sure the tests from the last exercise pass after the refactor
    3. Create a new CLI command that makes the tests below pass
    4. Ditto #2 above
    5. Your manager asks you to change the output of the hn-profile web view to bold the username in
       the output.  Make that change, adjust the tests from the last exercise and refactor existing
       code as needed (but not the current tests) to make sure all tests pass and the output in the
       browser and the CLI look as one would expect.
    6. Run the browser version and cli version to make sure it works for real too
    7. Properly handle an invalid username (e.g. 'rsyrin') being passed in (unhappy path).  Practice
       TDD, write tests first, watch them fail, then change code to make them pass.
    8. You are probably noticing the CLI and view logic look mostly the same, let's refactor to have
       use a common function (hackernews.profile_stats(username, use_html)) that both the cli
       function and view function can use.
"""
import pytest


class Tests:

    def test_cli_hn_profile(self, cli):
        # Hint: you will need to do some mocking
        result = cli.invoke('hn-profile', 'rsyring')
        assert result.output == 'HackerNews user rsyring has 3 submissions and 123 karma.\n'

        result = cli.invoke('hn-profile', 'foo')
        assert result.output == 'HackerNews user foo has 3 submissions and 123 karma.\n'
