import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGO_URI = os.environ.get("MONGO_URI")

    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


configs = {"local": LocalConfig, "production": ProductionConfig, "default": LocalConfig}
