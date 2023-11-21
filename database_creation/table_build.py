""" Class to insert / update tables as needed """

import mysql.connector
from utils import utils
from db_build import DbBuild
import names
import csv
import random


class TableBuild(DbBuild):
    def __init__(self,logger):
        DbBuild.__init__(self,logger)

    def _select_firstname(self):
        return names.get_first_name()

    def _build_users(self):
        """ Function to insert randomly generated variables into users table """
        TABLE_NAME = "users"
        COLS = ", ".join(utils["USER_COLS"])
        count = utils["desired_user_count"]

        names = [self._select_firstname()
                 for i in range(count)]

        ages = [random.randint(15, 85)
                for i in range(count)]

        genres = [random.choice(utils["MUSIC_STYLES"])
                  for i in range(count)]

        results = list(zip(names, ages, genres))
        query = utils["INSERT_STATEMENT"].format(TABLE_NAME, COLS)
        self.cursor.executemany(query, results)

        self.db.commit()
        #self.close_db()
        self.logger.info("\n*** Values inserted successfully to users table. ***\n")

    def _build_songs(self):
        """ Function to execute song table build from csv """
        TABLE_NAME = "songs"
        COLS = ", ".join(utils["SONG_COLS"])
        csv_data = csv.reader(open(utils["SONG_FILE"]))
        next(csv_data)
        query = utils["INSERT_STATEMENT"].format(TABLE_NAME, COLS)
        for row in csv_data:
            self.cursor.execute(query,row[1:])
        self.db.commit()

        self.logger.info("\n*** Values inserted successfully to songs table. ***\n")

    def build_tables(self):
        """ Function to execute build of other tables """
        try:
            self._build_users()
            self._build_songs()
            self.close_db()
        except Exception as e:
            self.logger.warning("\n***Error inserting values***\n")
            self.logger.warning(e)

        return None