from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.application.routes import application
    app.register_blueprint(application)

    from flaskblog.posts.routes import posts
    app.register_blueprint(posts)

    from flaskblog.users.routes import users
    app.register_blueprint(users)

    from flaskblog.errors.handlers import errors
    app.register_blueprint(errors)

    from flaskblog.calendar.routes import calendar
    app.register_blueprint(calendar)

    from flaskblog.battleboats.routes import battleboats
    app.register_blueprint(battleboats)

    return app
