import os
import sys

import unittest

import data_handling.db_handling as db_man

class test__handling(unittest.TestCase):
    """class to test the functionality of the module database_management
   in data_handling package"""
    
    
        

    def test_create_empty_sqlite_db(self):
        path=sys.path[0]
        test_class=db_man.Db_management(path)
        test_class.create_empty_sqlite_db('test')
        full_db_location=path+'\\'+'test.db'
        print(full_db_location)
        self.assertTrue(os.path.exists(full_db_location))

    def test_delete_sqlite_db(self):
        path=sys.path[0]
        test_class=db_man.Db_management(path)
        test_class.delete_sqlite_db('test')

    def test_connect_to_sqlite_db(self):
        path=sys.path[0]
        test_class=db_man.Db_management(path)
        test_class.create_empty_sqlite_db(path)
        engine=test_class.connect_to_sqlite_db('test')
        self.assertIsNotNone(engine)
        test_class.delete_sqlite_db('test')
        engine=test_class.connect_to_sqlite_db('test')
        self.assertIsNone(engine)
        





unittest.main()
        
    

