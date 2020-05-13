import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = '012345'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patricia:wanja2002@localhost/blogging101'
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    ''' 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patricia:wanja2002@localhost/blogging101'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/blogging101'

config_options = {
'development':DevConfig,
'production':ProdConfig
}
