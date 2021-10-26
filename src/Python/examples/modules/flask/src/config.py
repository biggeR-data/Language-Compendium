import os
from dotenv import load_dotenv

class Config(object):
    # Environment
    DEBUG = False
    TESTING = False

    SESSION_COOKIE_SECURE = False

    # loading Environment Variables
    load_dotenv()
    apikey = os.getenv("apikey")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True