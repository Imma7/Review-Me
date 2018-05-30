#import os module that allows our app to interact with the OS dependent functionality
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/reviewdb'

    @staticmethod
    def init_app(app):
        app



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/reviewdb'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}