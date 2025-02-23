import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
##################################
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

################################
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


def create_app():
    app.config.from_object(Config)
    login_manager.init_app(app)
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app
