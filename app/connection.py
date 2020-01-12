import sqlite3
import os
import sys
import env_file

class Connection(object):
    def __init__(self):
        envs = env_file.get('.env')
        file = './%s' % envs.get('DATABASE')
        
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