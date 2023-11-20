"""
Function to create connection to SQL and DB / table creation
"""

import mysql.connector
from utils import utils


class DbBuild:

    def __init__(self, logger):
        """Initialize the DB information"""
        self.__localhost = utils['HOST']
        self.__username = utils['USER']
        self.__password = utils['PASSWORD']
        self.__database_name = utils['DB']
        self.logger = logger
        self.create_db()
        self.create_connection()
        self.cursor = self.db.cursor()
        self.create_tables()
        self.db.commit()

    def create_db(self):
        """ Create DB """
        my_connection = mysql.connector.connect(
            host=self.__localhost,
            user=self.__username,
            passwd=self.__password
        )
        self.__conn = my_connection.cursor()
        self.__conn.execute("DROP DATABASE IF EXISTS %s" % self.__database_name)
        self.__conn.execute("CREATE DATABASE IF NOT EXISTS %s" % self.__database_name)
        self.logger.info("\n*** Database was created successfully. ***\n")

    def create_connection(self):
        """Create connection"""
        self.db = mysql.connector.connect(
            host=self.__localhost,
            user=self.__username,
            passwd=self.__password,
            database=self.__database_name
        )
        self.logger.info("\n*** Connection was created successfully. ***\n")

    def create_tables(self):
        """Create table statements"""
        for statement in ''.join(utils['CREATE_TABLE_STATEMENTS']).split(';'):
            try:
                self.cursor.execute(statement)
                self.logger.info('{} ---  executed successfully'.format(statement))
                self.db.commit()
            except Exception as err:
                self.logger.error(statement, '\n', err)

        self.db.commit()
        self.logger.info("\n*** Created tables successfully ***\n")

    def close_db(self):
        """Close mysql DB connection"""
        try:
            self.cursor.close()
            self.db.close()
            self.logger.info("\n*** MySQL connection is closed. ***\n")
        except Exception as err:
            self.logger.info("\n*** Connection to MySQL did not succeed to close {}. ***\n".format(err))

