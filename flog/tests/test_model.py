import flog.model.entities as ents


class TestPost:

    def test_insert(self, db):
        post = ents.Post(title='foo', author='bar', body='baz')
        db.session.add(post)
        db.session.commit()
        assert ents.Post.query.count() == 1
        assert ents.Post.query.first() is post
