import os 

from  sqlalchemy import create_engine

class Config(object):
    SECRET_KEY ="ClaveSecreta"
    SESSION_COOKIE_SEGURE=False
    

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:210804@127.0.0.1/bdidgs805'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
