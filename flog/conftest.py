import pytest
import requests

import flog.app
import flog.ext


@pytest.fixture(scope='session')
def app():
    app = flog.app.create_app(testing=True)

    flog.ext.db.drop_all(app=app)
    flog.ext.db.create_all(app=app)

    return app


@pytest.fixture()
def cli(app):
    return app.test_cli_runner()


@pytest.fixture()
def db(app):
    with app.app_context():
        yield flog.ext.db
        flog.ext.db.session.remove()


@pytest.fixture()
def web(app):
    return app.test_client()


@pytest.fixture()
def fetch_mail(app):
    url = 'http://localhost:1080/api/emails'
    requests.delete(url)
    app.extensions['mail'].suppress = False
    yield lambda: requests.get(url, timeout=2.0).json()
    app.extensions['mail'].suppress = True
