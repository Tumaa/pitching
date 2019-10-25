import os

class Config:
    SECRET_KEY = '123456'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fatuma:qwerty12@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    

    #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    DEBUG = True

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fatuma:qwerty12@localhost/tuma00'


class TestConfig(Config):
   '''
   Testing configuration child class
  
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fatuma:qwerty12@localhost/tuma00'

   pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fatuma:qwerty12@localhost/tuma00'
    

    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
    }