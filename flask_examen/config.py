import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-me'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:////sqlite3-db/app.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False