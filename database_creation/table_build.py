""" Class to insert / update tables as needed """

import mysql.connector
from utils import utils
from db_build import DbBuild
import names
import random

class TableBuild(DbBuild):
    def __init__(self,logger):
        DbBuild.__init__(self,logger)

    def _select_firstname(self):
        return names.get_first_name()


    def build_table(self):
        count = utils["desired_user_count"]
        try:
            names = [self._select_firstname()
                     for i in range(count)]

            ages = [random.randint(15, 85)
                    for i in range(count)]

            genres = [random.choice(utils["MUSIC_STYLES"])
                      for i in range(count)]

            results = list(zip(names,ages,genres))
            query = utils["INSERT_STATEMENT"]
            self.cursor.executemany(query, results)

            self.db.commit()
            self.close_db()

            self.logger.info("\n*** Values inserted successfully. ***\n")
        except:
            self.logger.warning("\n***Error inserting values***\n")

        return None