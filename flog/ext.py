from flask_sqlalchemy import SQLAlchemy
from flask_mailman import Mail

db = SQLAlchemy()
mail = Mail()


def init_ext(app):
    db.init_app(app)
    mail.init_app(app)
