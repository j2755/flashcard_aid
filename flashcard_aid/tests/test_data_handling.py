import os
import sys

import unittest

import data_handling.database_management as db_man
import data_handling.table_management as tbl_man
class test_data_handling(unittest.TestCase):
    """class to test the functionality of the module database_management
   in data_handling package"""

    def test_create_connection(self):
        path=sys.path[0]
        test_class=db_man.Db_management(path)
        test_class.create_connection('test')
        full_db_location=path+'\\'+'test.db'
        print(full_db_location)
        self.assertTrue(os.path.exists(full_db_location))
        

class test_table_management(unittest.TestCase):
    """class to test the functionality of the module table_management 
    in data_handling_package"""

    def test_connect_to_sqlite_db(self):
        path=sys.path[0]
        test_class=db_man.Db_management(path)
        test_class.create_connection('test')
        full_db_location=path+'\\'+'test.db'



unittest.main()
        
    

