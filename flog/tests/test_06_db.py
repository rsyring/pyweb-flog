"""
    Principle #12: (reminder) tests are responsible for managing expected state (usually at the
        start of the test)
    Principle #13: the start of a test run should always clear & recreate the db schema
    Principle #14: generators are always better than database data fixtures
    Principle #15: magic generators are really cool

    Exercises:

    1. Use a pytest fixture to clear the tables before each test run
    2. Create a testing_create() method on the entity classes to make it easy to generate
        test data
    3. Integrate a [magic] testing create method instead

    [magic]: https://github.com/rsyring/bookorders/blob/master/bookorders/model/utils.py#L125
"""
import pytest

import flog.model.entities as ents


class Tests:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        ents.Post.query.delete()
        db.session.commit()

    def test_comment(self, db):
        comment = ents.Comment.testing_create()
        assert ents.Post.query.count() == 1
        assert ents.Post.query.first() is comment.post

        assert ents.Comment.query.count() == 1
        assert ents.Comment.query.first() is comment

    def test_post(self, db):
        post = ents.Post.testing_create()
        assert ents.Post.query.count() == 1
        assert ents.Post.query.first() is post
