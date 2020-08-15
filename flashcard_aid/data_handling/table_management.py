import sqlite3
from sqlite3 import Error

import sqlalchemy
import sqlalchemy_utils
import pandas


class tbl_management():
    """add,edit, and delete tables from an existing database"""
    def __init__(self,db_file_location):
        self.loc=db_file_location
        self.engine=connect_to_sqlite_db(self.loc)


    def connect_to_sqlite_db(self):
        if sqlalchemy_utils.database_exists(self.loc):
            engine = create_engine('sqlite:///'+location)
        else:
            sqlalchemy_utils.create_database(self.loc)
            engine = create_engine('sqlite:///'+location)
        return engine

    def read_table(self,table_name):
        self.engine.connect()
        metadata = sqlalchemy.MetaData()
        tbl_data = db.Table(table_name, metadata, autoload=True, autoload_with=self.engine)
        return tbl_data

