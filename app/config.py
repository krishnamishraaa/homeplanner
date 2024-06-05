class Config(object):
    DEBUG = False
    TESTING = False
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_TIMEOUT = 300

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = "debugkeyistruehowcanitbefalse"
    SECURITY_PASSWORD_SALT = "saltedthepasswordsforsecurity"
    SQLALCHEMNY_TRACK_MODIFICATION  = False
    WTF_CSRF_ENABLED = False
    