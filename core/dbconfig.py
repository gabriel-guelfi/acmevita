from .app import app
from flask_sqlalchemy import SQLAlchemy
from os import environ as env

class Dbconfig:
    # Class Contructor
    def __init__(self):
        """

        This method set the options received on 
        parameter "configs" on the Database Configs
        property and return an instance of the 
        Dbconfig class 

        """

        self.__configs = {}
        self.__configs['dbuser'] = env['DBUSER']
        self.__configs['dbpass'] = env['DBPASS']
        self.__configs['dbname'] = env['DBNAME']
        self.__configs['dbhost'] = env.get("DBHOST", "localhost")
        self.__configs['dbport'] = int(env.get("DBHOST", "3306"))
        
    # Getter for Database Configs
    @property
    def configs(self):
        """

        Returns the current database settings

        """

        return self.__configs

    # Method that starts the ORM
    def startDB(self):
        """
        
        Initiate ORM, passing along the database settings, then
        returns the instance of the ORM, which was created with 
        those settings.
        
        """

        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(self.configs['dbuser'], self.configs['dbpass'], self.configs['dbhost'], self.configs['dbport'], self.configs['dbname'])
        return SQLAlchemy(app)