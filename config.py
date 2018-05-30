#import os module that allows our app to interact with the OS dependent functionality
import os

class Config:
    SECRET_KEY = os.urandom(15)


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLE_USE_CDN = True

    @staticmethod
    def init_app(app):
        app



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/reviewdb'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}