from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from .routes import configure_routes
import os
import json

from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app, origins="*")

    private_key = os.getenv("PRIVATE_KEY").replace("\\n", "\n")

    firebase_creds = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": private_key,
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN")
    }

    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

    configure_routes(app)

    return app
