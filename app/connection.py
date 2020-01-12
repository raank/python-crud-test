import sqlite3
import os
import sys
import config

class Connection(object):
    def __init__(self, tests=False):
        if tests:
            db_file = config.get('database_tests')
        else:
            db_file = config.get('database')
        
        file = './%s' % db_file
        
        try:
            self.conn = sqlite3.connect(file)
            
            if self.conn is None:
                print('Connection is closed')
        except Exception as err:
            print('Connection failed.: %s' % err)
        
    def close(self):
        if self.conn:
            self.conn.close()
            print('Connection closed')
            
    def cursor(self):
        return self.conn.cursor()
    
    def commit(self):
        return self.conn.commit()