import os
import sqlite3
from sqlite3 import Error

import sqlalchemy
from sqlalchemy import Table,Column
from sqlalchemy import MetaData

import pandas


class Db_management():
    """generic functionality for creation and modification of databases and tables"""
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

    def create_sqlite_engine(self,name):
        full_name=self.loc+'\\'+name+'.db'
        if os.path.exists(full_name):
            engine = sqlalchemy.create_engine('sqlite:///'+full_name)
            return engine
        else:
      
            return None
    
    def create_empty_table(self,db_name,table_name):
        """" useless function, only useful to test get_list_of_tables"""
        engine=self.create_sqlite_engine(db_name)
        meta=MetaData()
        table=sqlalchemy.Table(table_name,meta,Column('id', sqlalchemy.Integer, primary_key = True))
        meta.create_all(engine) 
    def get_list_of_tables(self,db_name):
        engine=self.create_sqlite_engine(db_name)
        return engine.table_names()



    def read_table(self,db_name,table_name):
        engine=self.create_sqlite_engine(db_name)
        self.engine.connect()
        metadata = MetaData()
        tbl_data = db.Table(table_name, metadata, autoload=True, autoload_with=self.engine)
        return tbl_data


