import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wealthpath_super_secret_key_123'
    MYSQL_HOST = "localhost"
    MYSQL_USER = "wealthuser"
    MYSQL_PASSWORD = "kinjal123"
    MYSQL_DB = "wealthpath"