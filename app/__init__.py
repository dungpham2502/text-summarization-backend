from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from .routes import configure_routes


def create_app():
    app = Flask(__name__)
    CORS(app, origins="*")

    cred = credentials.Certificate('credentials.json')
    firebase_admin.initialize_app(cred)

    configure_routes(app)

    return app
