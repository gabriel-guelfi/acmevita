from .app import app
from flask_sqlalchemy import SQLAlchemy

class Dbconfig:

    def __init__(self, configs):
        self.__configs = configs

    @property
    def configs(self):
        return self.__configs

    def startDB(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(self.configs['dbuser'], self.configs['dbpass'], self.configs['dbhost'], self.configs['dbport'], self.configs['dbname'])
        return SQLAlchemy(app)