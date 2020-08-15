import os
import sqlite3
from sqlite3 import Error

import sqlalchemy
import sqlalchemy_utils
import pandas


class Db_management():
    """manage databases  allow for the easy creation,deletion,and modification 
    of the databases"""
    def __init__(self,db_file_location):
        self.loc=db_file_location
        

    def create_empty_sqlite_db(self,name):
        """ create a database connection to a SQLite database """
        conn = None
        full_name=self.loc+'\\'+name+'.db'
        try:
            conn = sqlite3.connect(full_name)
            
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
    def delete_sqlite_db(self,name):
        full_name=self.loc+'\\'+name+'.db'
        os.remove(full_name)

    def connect_to_sqlite_db(self,name):
        full_name=self.loc+'\\'+name+'.db'
        if os.path.exists(full_name):
            engine = sqlalchemy.create_engine('sqlite:///'+full_name)
            return engine
        else:
            
            print('does not exist')  

    def read_table(self,table_name):
        self.engine.connect()
        metadata = sqlalchemy.MetaData()
        tbl_data = db.Table(table_name, metadata, autoload=True, autoload_with=self.engine)
        return tbl_data

