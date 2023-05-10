from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from eda_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER']=app.root_path


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail(app)

from eda_app.users.routes import users
from eda_app.cards.routes import cards

app.register_blueprint(users)
app.register_blueprint(cards)