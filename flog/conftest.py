import pytest

import flog.app
import flog.ext


@pytest.fixture(scope='session')
def app():
    app = flog.app.create_app()
    app.testing = True

    flog.ext.db.drop_all(app=app)
    flog.ext.db.create_all(app=app)

    return app


@pytest.fixture()
def cli(app):
    return app.test_cli_runner()


@pytest.fixture()
def db(app):
    with app.app_context():
        yield flog.app.db
        flog.app.db.session.remove()


@pytest.fixture()
def web(app):
    return app.test_client()
