class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='developersjunior0@gmail.com'
    MAIL_PASSWORD='Nairobi001'
    
    
class ProdConfig(Config):
   '''
   Pruduction configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
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
