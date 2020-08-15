import sqlite3
from sqlite3 import Error


class Db_management(object):
    """initialize and modify database files"""
    def __init__(self,db_file_location):
 
        self.loc=db_file_location

    def create_connection(self,db_name):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.loc+'\\'+db_name+'.db')
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()



