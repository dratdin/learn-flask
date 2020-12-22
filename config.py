import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGO_URI = os.environ.get("MONGO_URI")
    MONGO_HOST = os.environ.get("MONGO_HOST")
    MONGO_PORT = os.environ.get("MONGO_PORT")
    SESSION_TYPE = "mongodb"

    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


configs = {"local": LocalConfig, "production": ProductionConfig, "default": LocalConfig}
