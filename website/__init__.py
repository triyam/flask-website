from flask import Flask
from pymongo import MongoClient
import urllib

def create_app():
    app = Flask(__name__)
    app.secret_key = 'testing'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app