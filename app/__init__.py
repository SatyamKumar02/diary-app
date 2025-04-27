from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

login_manager = LoginManager()
login_manager.login_view = 'login'
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database("diary_app")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    login_manager.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
